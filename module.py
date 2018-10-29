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
    password = Column(String(20))