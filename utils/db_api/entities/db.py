import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


logging.basicConfig(format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
                    level=logging.INFO)

DB_NAME = "db.sqlite"
url = f"sqlite:///{DB_NAME}"
engine = create_engine(url, echo=True, future=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()


def create_db():
    Base.metadata.create_all(engine)