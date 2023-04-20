from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

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


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer(text=f'Version {VERSION}')
    if message.from_user.id == BOT_ADMIN:
        await message.answer(
            text=f'Привет, администратор {BOT_ADMIN}\n'
                 f'{ADMIN_COMMANDS}')
    else:
        await message.answer(text=f'Привет, пользователь {message.from_user.id}')


@dp.message(Command(commands=['all_keys']), IsAdmin(BOT_ADMINS))
async def process_get_all_keys(message: Message):
    if message.from_user.id == BOT_ADMIN:
        response = print_outline_users(get_all_users())
        await message.answer(text=response)
    else:
        await message.answer(text='Вы не являетесь администратором бота!')


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


@dp.message(IsAdmin(BOT_ADMINS))
async def admin_wrong_answer(message: Message):
    await message.answer(text='Неверная команда')


@dp.message()
async def not_admin_answer(message: Message):
    await message.answer(text='Вы не являетесь администратором!')


if __name__ == '__main__':
    dp.run_polling(bot)
