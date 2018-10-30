<<<<<<< HEAD
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
# 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    name = Column(String(20), primary_key=True)
=======
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
# 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    name = Column(String(20), primary_key=True)
>>>>>>> 9b75f101837b0882f167be488a4c31294b8cf351
    password = Column(String(20))