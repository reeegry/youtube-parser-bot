from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Boolean
from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    yt_parent = relationship("Youtube", back_populates="yt_child")
    tw_parent = relationship("Twitch", back_populates="tw_child")

    def __repr__(self):
        return f"<User({self.id=}, {self.tg_id}, {self.status=})>"