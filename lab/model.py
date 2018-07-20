from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	""" Copy your Knowledge class from knowledge_model.py here! """
	__tablename__ = 'knowledge'
	article_id = Column(Integer, primary_key=True)
