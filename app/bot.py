from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from app.classes import OutlineUser
from app.manager import get_all_users, get_new_user
from app.services import print_outline_users
from app.settings import BOT_ADMIN, BOT_TOKEN


API_TOKEN: str = BOT_TOKEN
BOT_ADMIN: int = int(BOT_ADMIN)

ADMIN_COMMANDS: str = ('/all_keys - Показать все ключи доступа\n'
                       '/new_key - Создать новый ключ\n'
                       '/start - старт')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    if message.from_user.id == BOT_ADMIN:
        await message.answer(
            text=f'Привет, администратор {BOT_ADMIN}\n'
                 f'{ADMIN_COMMANDS}')
    else:
        await message.answer(text=f'Привет, пользователь {message.from_user.id}')


@dp.message(Command(commands=['all_keys']))
async def process_get_all_keys(message: Message):
    if message.from_user.id == BOT_ADMIN:
        response = print_outline_users(get_all_users())
        await message.answer(text=response)
    else:
        await message.answer(text='Вы не являетесь администратором бота!')


@dp.message(Command(commands=['new_key'], ))
async def process_new_key(message: Message):
    if message.from_user.id == BOT_ADMIN:
        new_user: OutlineUser = get_new_user()
        response = print_outline_users(new_user)
        await message.answer(text=response)
        await message.answer(text=new_user.accessUrl)
    else:
        await message.answer(text='Вы не являетесь администратором бота!')



if __name__ == '__main__':
    dp.run_polling(bot)
