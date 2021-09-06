from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.schema import ForeignKey
from .user import User
from .db import Base


class Twitch(Base):
    __tablename__ = "twitch"

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    channel_name = Column(String)
    send_message = Column(Boolean, default=False)
    tw_child = relationship("User", back_populates="tw_parent")

    def __repr__(self):
        return f"<TwitchTable({self.user_id=}, {self.channel_name=}, {self.send_message=})>"