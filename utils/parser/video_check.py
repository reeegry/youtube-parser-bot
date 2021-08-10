import asyncio
from .youtube_api_parser import get_information
from ..db_api.db_sqlite3 import *


async def periodic():
    while True:
        await asyncio.sleep(10)

        for user in db.get_subscriptions():
            user_id = user[1]
            channel_id = user[3]
            video_title = user[5]

            try:
                video_title_new, video_url_new = get_information(channel_id)
                if video_title_new != video_title and video_title != "None":
                    db.change_send_message_status(user_id, send_message=True)
                db.update_video_title(user_id, video_title_new)
                db.update_video_url(user_id, video_url_new)
            except:
                logging.error("something went wrong.")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

