from .entities.db import create_db
from .entities.twitch import Twitch
from .entities.youtube import Youtube
from .entities.user import User
from . import db_funcs


create_db()
# db_funcs.add_user(42, "foo")
print(db_funcs.user_exist(21))
# print(db_funcs.get_data())
