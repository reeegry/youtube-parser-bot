from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types.input_file import InputFile
from data.photo import *
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    photo1 = InputFile("data/photo/1.png")
    photo2 = InputFile("data/photo/2.png")

    await message.answer(f"Hello, {message.from_user.full_name}! Enter youtube channel link"
                         "from which you want to receive updates.")
    await dp.bot.send_photo(photo=photo1, chat_id=message.chat.id)
    await dp.bot.send_photo(photo=photo2, chat_id=message.chat.id)
