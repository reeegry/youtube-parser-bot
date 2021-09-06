from aiogram import types

from loader import dp
from utils.db_api import db_funcs


async def check_channel_exist(user_id, message: types.Message):
    for data in db_funcs.get_data():
        if message.text == data.Youtube.channel_id and user_id == data.User.tg_id:
            return True
        return False


@dp.message_handler(state=None)
async def echo(message: types.Message):
    user_id = message.from_user.id
    if not db_funcs.user_exist(user_id):
        db_funcs.add_data(user_id)
    
    channel_exist = await check_channel_exist(user_id, message)
    if not channel_exist:
        # TODO: change func to youtube_add
        db_funcs.youtube_add(tg_id=user_id, channel_id=message.text, last_video_title="None")
    await message.answer(f"Added")

