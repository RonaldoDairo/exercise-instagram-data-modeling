import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Media(Base):
        __tablename__ = 'media'
        ID = Column(Integer, primary_key=True)
        type =Column(String(250))
        url = Column(String(250))
        post_id = Column(Integer)
    
class Comment(Base):
        __tablename__ = 'comment'
        ID = Column(Integer, primary_key=True)
        comment_text = Column(String(250))
        author_id = Column(Integer)
        post_id = Column(Integer)
        
class Follower(Base):
        __tablename__ = 'follower'
        user_from_id = Column(Integer ,primary_key = True)  
        user_to_id = Column(Integer)  

class Post(Base):
        __tablename__ = 'post'
        user_id = Column(Integer) 
        ID = Column(Integer, primary_key=True, foreign_keys=[ForeignKey('comment.post_id'), ForeignKey('media.post_id')])
        comment = relationship(Comment)
    
class User(Base):
        __tablename__ = 'user'
        ID = Column(Integer, primary_key=True )
        user_name= Column(String(250), unique = True )
        firstname = Column(String(250), ) 
        lastname =  Column(String(250),)
        email = Column(String(250), unique = True)
        person_id = Column(Integer, ForeignKey('follower.user_from_id ,'),
         ForeignKey('follower.user_to_id'), ForeignKey('comment.author_id'), ForeignKey('post.user_id') )
        person = relationship(Follower)
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
