from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Старт'),
        BotCommand(command='/all_keys',
                   description='Показать все ключи доступа'),
        BotCommand(command='/new_key',
                   description='Создать новый ключ'),
        BotCommand(command='/all_keys_list',
                   description='Список всех ключей')
    ]

    await bot.set_my_commands(main_menu_commands)
