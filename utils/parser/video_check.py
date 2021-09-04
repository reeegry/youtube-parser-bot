import logging
import asyncio
from .parser import youtube_get_information
from ..db_api import db_funcs


async def periodic():
    while True:
        await asyncio.sleep(10)

        for user in db_funcs.get_data():
            tg_id = user.User.tg_id
            channel_id = user.Youtube.channel_id
            video_title = user.Youtube.last_video_title

            try:
                video_title_new, video_url_new = youtube_get_information(channel_id)
                if video_title_new != video_title and video_title != "None":
                    db_funcs.change_send_message_status(tg_id, send_message=True)
                db_funcs.youtube_update(tg_id=tg_id, last_video_title=video_title_new, 
                    last_video_url=video_url_new)
            except:
                logging.error("something went wrong.")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

