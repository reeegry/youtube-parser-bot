from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
host = env.str("host")
PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")
YOUTUBE_API_KEY = env.str("YOUTUBE_API_KEY")
CLIENT_ID = env.str("CLIENT_ID")
SECRET = env.str("SECRET")