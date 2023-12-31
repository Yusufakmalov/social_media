from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    profile_photo = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)

# Table of posts
class UserPost(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_text = Column(String)
    publish_date = Column(DateTime)
# conecting to the User, lazy is need to show elements in Users when it should do it
    user_fk = relationship(User, lazy="subquery")

class PostPhoto(Base):
    __tablename__ = 'post_photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    post_photo = Column(String)

    post_fk = relationship(UserPost, lazy="subquery")

class Comment(Base):
    __tablename__ = 'post_comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey('user_posts.id'))
    comment_text = Column(String)

    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserPost, lazy="subquery")