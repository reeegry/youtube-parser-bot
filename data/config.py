from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
host = env.str("host")
PG_USER = env.str("PG_USER")
PG_PASS = env.str("PG_PASS")
