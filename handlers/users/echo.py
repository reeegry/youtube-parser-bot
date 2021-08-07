from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils.db_api.db_sqlite3 import *


@dp.message_handler(state=None)
async def echo(message: types.Message):
    user_id = message.from_user.id
    if not db.subscriber_exists(user_id):
        db.add_subscriber(user_id)
    else:
        db.update_subscription(user_id, True)
    db.update_channel(user_id, message.text)
    await message.answer(f"добавлен")


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
