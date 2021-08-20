from aiogram import types

from loader import dp
from utils.db_api.db_sqlite import *


@dp.message_handler(state=None)
async def echo(message: types.Message):
    user_id = message.from_user.id
    if not db.subscriber_exists(user_id):
        db.add_subscriber(user_id)
    else:
        db.update_subscription(user_id, True)
    db.update_channel_id(user_id, message.text)
    db.update_video_title(user_id, "None")
    await message.answer(f"Added")

