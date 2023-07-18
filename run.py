from src.bot import bot, dp
from src.bot_menu import set_main_menu

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)
