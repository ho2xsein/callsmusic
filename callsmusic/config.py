from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = '386893380:AAGQzP4kmQSayOkYs6jp7AV_q3dI5ihNpaQ'
API_ID = 5378568
API_HASH = '89ffcb590951a70b2f00d51a3689458b'
DURATION_LIMIT = 10
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
