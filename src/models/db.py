
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, Text, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# configuration

engine = create_engine("sqlite:///teste.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()