from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime


Base = declarative_base()
db = create_engine('sqlite:///telebot.db')
session = Session(bind=db)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    chat_id = Column(Integer)
    description = Column(String(255), nullable=False)
    path = Column(String(100))
    url = Column(Text)
    create_on = Column(DateTime(), default=datetime.today())


Base.metadata.drop_all(db)
Base.metadata.create_all(db)
