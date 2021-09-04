import asyncio
from loader import dp, scheduler
from .db_api import db_funcs


async def send_message_if_new_video(dp):
    for user in db_funcs.get_data():
        send_message = user.Youtube.send_message
        tg_id = user.User.tg_id
        channel_id = user.Youtube.channel_id
        last_video_url = user.Youtube.last_video_url
        last_video_title = user.Youtube.last_video_title

        if send_message:
            await dp.bot.send_message(tg_id, f"new video on channel with id{channel_id}: "
                                                     f"{last_video_title} ({last_video_url})")
            db_funcs.change_yt_send_message_status(tg_id, send_message=False)


def scheduler_jobs():
    scheduler.add_job(send_message_if_new_video, "interval", seconds=5, args=(dp, ))
    scheduler.start()
