import asyncio
from loader import dp, scheduler
from .db_api import db_funcs


async def send_message_if_new_video(dp):
    pass
    # for user in db.get_data():
    #     send_message = user[-1]
    #     user_id = user[1]
    #     channel_id = user[2]
    #     last_video_url = user[3]
    #     last_video_title = user[4]

    #     if send_message:
    #         await dp.bot.send_message(user_id, f"new video on channel with id{channel_id}: "
    #                                            f"{last_video_title}({last_video_url})")
    #         db.youtube_table.change_send_message_status(user_id, send_message=False)


def scheduler_jobs():
    scheduler.add_job(send_message_if_new_video, "interval", seconds=5, args=(dp, ))
    scheduler.start()
