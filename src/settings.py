import os
from dotenv import load_dotenv

load_dotenv()

APIURL = os.getenv('APIURL')
APICERT = os.getenv('APICERT')

BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_ADMIN = os.getenv('BOT_ADMIN')

adminlist: list = BOT_ADMIN.split(', ')
BOT_ADMINS: list[int] = list(map(int, adminlist))

VERSION = '1.02'
