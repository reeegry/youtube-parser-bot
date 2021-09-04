from sqlalchemy import and_
from .entities.twitch import Twitch
from .entities.youtube import Youtube
from .entities.user import User
from .entities.db import session


def get_data():
    return session.query(User, Youtube, Twitch).filter(User.id==Youtube.user_id).all()


def user_exist(tg_id):
    return session.query(User, Youtube, Twitch).filter(and_(User.id==Youtube.user_id, 
                                                            User.tg_id==tg_id)).first()


def add_data(tg_id, channel_id = None, last_video_url = None, status = True):
    user = User(tg_id=tg_id, status=False)
    youtube = Youtube(channel_id=channel_id, last_video_url=last_video_url)
    twitch = Twitch()
    user.yt_parent, user.tw_parent = [youtube], [twitch]
    session.add_all([user, youtube, twitch])
    session.commit()


def youtube_add(user_id, channel_id = Youtube.channel_id, 
        last_video_title = Youtube.last_video_title):
    # youtube = Youtube(user_id=user_id, channel_id=channel_id, last_video_title=last_video_title)
    # session.add([youtube])
    # session.commit()
    pass


def change_yt_send_message_status(tg_id, status):
    db_user_id = session.query(User.id).filter(User.tg_id==tg_id).first()[0]
    session.query(Youtube).filter(Youtube.user_id==db_user_id).update({"status": status})
    session.commit()


def youtube_update(tg_id, channel_id = Youtube.channel_id, 
        last_video_title = Youtube.last_video_title, 
        last_video_url = Youtube.last_video_url):
    db_user_id = session.query(User.id).filter(User.tg_id==tg_id).first()[0]

    session.query(Youtube).filter(Youtube.user_id==db_user_id). \
        update(
            {"last_video_title": last_video_title, 
            "channel_id": channel_id, 
            "last_video_url": last_video_url})
    session.commit()


def user_exist(tg_id):
    return session.query(User).filter(User.tg_id==tg_id).first()


# if session.query(User).filter(User.tg_id=="564126822").first():
#     print(1)

# for item in session.query(User):
#     print(item)

