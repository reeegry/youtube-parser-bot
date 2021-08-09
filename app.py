from aiogram import executor

# from data.config import *
from utils.parser import video_check
from loader import dp, scheduler
from utils.db_api.db_sqlite3 import db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    scheduler_jobs()


async def send_message_if_new_video(dp):
    for user in db.get_subscriptions():
        send_message = user[-1]
        user_id = user[1]
        channel = user[3]
        last_video_url = user[4]
        last_video_title = user[5]

        if send_message:
            await dp.bot.send_message(user_id, f"new video on channel {channel}: {last_video_title}({last_video_url})")
            db.change_send_message_status(user_id, send_message=False)


def scheduler_jobs():
    scheduler.add_job(send_message_if_new_video, "interval", seconds=5, args=(dp, ))


if __name__ == "__main__":
    scheduler.start()
    video_check.loop.create_task(video_check.periodic())
    executor.start_polling(dp, on_startup=on_startup)



