from aiogram import types

from loader import dp
from utils.db_api.db_sqlite import *


async def channel_exist(user_id, message: types.Message):
    for data in db.get_data():
        channel_id, db_user_id = data[3], data[0]
        if message.text == channel_id and user_id == db_user_id:
            return True
        return False


@dp.message_handler(state=None)
async def echo(message: types.Message):
    user_id = message.from_user.id
    if not db.subscriber_exists(user_id):
        db.add_subscriber(user_id)
    else:
        db.update_subscription(user_id, True)
    
    if not channel_exist(user_id, message):
        db.youtube_table.insert_youtube_data(user_id, message.text, "None") 
    await message.answer(f"Added")

