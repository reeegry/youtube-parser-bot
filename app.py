from aiogram import executor

from utils.parser import video_check
from loader import dp
from utils import send_message_if_new_video
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api import db_creator


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    video_check.loop.create_task(video_check.periodic())
    send_message_if_new_video.scheduler_jobs()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)



