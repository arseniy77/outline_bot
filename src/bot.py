from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (InlineKeyboardButton, KeyboardButton, Message,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           CallbackQuery)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot_filters import IsAdmin, KeyNameInNewKeyCommand
from src.classes import OutlineUser
from src.manager import get_all_users, get_new_user
from src.services import print_outline_users
from src.settings import BOT_ADMIN, BOT_ADMINS, BOT_TOKEN, VERSION

API_TOKEN: str = BOT_TOKEN
BOT_ADMIN: int = int(BOT_ADMIN)

ADMIN_COMMANDS: str = ('/all_keys - Показать все ключи доступа\n'
                       '/new_key - Создать новый ключ\n'
                       '/start - старт')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

button_all_keys: KeyboardButton = KeyboardButton(text='/all_keys')
button_new_key: KeyboardButton = KeyboardButton(text='/new_key')
button_start: KeyboardButton = KeyboardButton(text='/start')

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_start], [button_all_keys, button_new_key]],
    resize_keyboard=True,
)


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text=f'Version {VERSION}')
    if message.from_user.id == BOT_ADMIN:
        await message.answer(
            text=f'Привет, администратор {BOT_ADMIN}\n'
                 f'{ADMIN_COMMANDS}',
            reply_markup=keyboard)
    else:
        await message.answer(
            text=f'Привет, пользователь {message.from_user.id}')


@dp.message(Command(commands=['all_keys']), IsAdmin(BOT_ADMINS))
async def process_get_all_keys(message: Message):
    if message.from_user.id == BOT_ADMIN:
        response = print_outline_users(get_all_users())
        await message.answer(text=response,
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Вы не являетесь администратором бота!',
                             reply_markup=ReplyKeyboardRemove())


@dp.message(Command(commands=['new_key'], ), KeyNameInNewKeyCommand())
async def process_new_key(message: Message, name: str | None):
    if message.from_user.id == BOT_ADMIN:
        if name:
            new_user: OutlineUser = get_new_user(name)
        else:
            new_user: OutlineUser = get_new_user()
        response = print_outline_users(new_user)
        await message.answer(text=response)
        await message.answer(text=new_user.accessUrl)
    else:
        await message.answer(text='Вы не являетесь администратором бота!')


@dp.message(Command(commands=['all_keys_list'],), IsAdmin(BOT_ADMINS))
async def process_all_keys_list(message: Message):

    all_users_list: list[OutlineUser] = get_all_users()
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = [
        InlineKeyboardButton(
            text=user.name,
            callback_data=f'button_{user.name}_pressed'
        ) for user in all_users_list
    ]
    kb_builder.row(*buttons, width=1)

    await message.answer(
        text='Список пользователей',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


@dp.callback_query(F.data.startswith('button_'))
async def callback_test(callback: CallbackQuery):
    await callback.message.answer(
        text='test',
        show_alert=True
    )


@dp.message(IsAdmin(BOT_ADMINS))
async def admin_wrong_answer(message: Message):
    await message.answer(text='Неверная команда')


@dp.message()
async def not_admin_answer(message: Message):
    await message.answer(text='Вы не являетесь администратором!')


if __name__ == '__main__':
    dp.run_polling(bot)
