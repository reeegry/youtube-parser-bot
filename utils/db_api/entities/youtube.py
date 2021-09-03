from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy.sql.schema import ForeignKey
from .db import Base


class Youtube(Base):
    __tablename__ = "youtube"
	
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    channel_id = Column(String)
    last_video_title = Column(String)
    last_video_url = Column(String, nullable=False, default="None")
    send_message = Column(Boolean, default=False)
    # yt_child = relationship("User")

    def __repr__(self):
        return f"<YoutubeTable({self.channel_id=}, {self.last_video_title=}, \
                {self.last_video_url=}, {self.send_message=})>"