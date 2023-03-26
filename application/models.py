from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()


class Students(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(63), unique=True)
    percent = Column(Integer)


def getsession():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
