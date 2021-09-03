from aiogram import types

from loader import dp
from utils.db_api import db_funcs


async def check_channel_exist(user_id, message: types.Message):
    for data in db_funcs.get_data():
        print(data)
        return False
        # if message.text == data["channel_id"] and user_id == data["tg_id"]:
        #     return True
        # return False


@dp.message_handler(state=None)
async def echo(message: types.Message):
    user_id = message.from_user.id
    if not db_funcs.user_exist(user_id):
        db_funcs.add_data(user_id)
    
    channel_exist = await check_channel_exist(user_id, message)
    if not channel_exist:
        db_funcs.youtube_update(user_id, message.text, "None")
    await message.answer(f"Added")

