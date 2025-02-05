import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get(""))
    API_HASH = os.environ.get("")
    AUTH_USERS = os.environ.get("")
