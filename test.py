from flask import Flask, request, render_template, jsonify
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def default():
    return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    Username = request.form.get('username')
    Password = request.form.get('password')
    # 创建对象的基类:
    Base = declarative_base()
    # 定义User对象:
    class User(Base):
    # 表的名字:
        __tablename__ = 'user'
    # 表的结构:
        name = Column(String(20), primary_key=True)
        password = Column(String(20))

    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/FY')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        User = session.query(User).filter(User.name == '%s' % Username).one()
    except Exception as e:
        print(e)
        session.close()
        return jsonify({'result':'null'})
    session.close()
    if Password != User.password:
        return jsonify({'result':False})
    return jsonify({'result':True})

@app.route('/register', methods=['POST'])
def register():
    Username = request.form.get('username')
    Password = request.form.get('password')
    # 创建对象的基类:
    Base = declarative_base()
    # 定义User对象:
    class User(Base):
    # 表的名字:
        __tablename__ = 'user'
    # 表的结构:
        name = Column(String(20), primary_key=True)
        password = Column(String(20))

    # 建立连接，数据库
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/FY')
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    # 查找数据
    try:
        User = session.query(User).filter(User.name == '%s' % Username).one()
    except Exception as e:
        print(e)
        # 插入数据
        new_user = User(name=Username, password=Password)
        session.add(new_user)
        # 提交事务
        session.commit()
        # 关闭游标和连接
        session.close()
        return jsonify({'result':True})
    if Username == User.name:
        return jsonify({'result':False})

@app.route('/post', methods=['GET', 'POST'])
def post():
    Title = request.form.get('title')
    Context = request.form.get('context')
    Username = request.form.get('username')
    Time = request.form.get('time')
	# 创建对象的基类:
    Base = declarative_base()
    # 定义Post对象:
    class Post(Base):
    # 表的名字:
        __tablename__ = 'post'
    # 表的结构:
        name = Column(String(20), primary_key=True)
        title = Column(String(100))
        context = Column(String(10000))
        time = Column(String(20))
    # 建立连接，数据库
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/FY')
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
	# 插入数据
    new_post = Post(name=Username, title=Title, context=Context, time=Time)
    session.add(new_post)
    # 提交事务
    session.commit()
    # 关闭游标和连接
    session.close()
    return jsonify({'result':True})

@app.route('/newpage', methods=['GET', 'POST'])
def notice():
    Title = request.form.get('title')
    Username = request.form.get('username')
	# 创建对象的基类:
    Base = declarative_base()
    # 定义Post对象:
    class Post(Base):
    # 表的名字:
        __tablename__ = 'post'
    # 表的结构:
        name = Column(String(20), primary_key=True)
        title = Column(String(100))
        context = Column(String(10000))
        time = Column(String(20))
    # 建立连接，数据库
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/FY')
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
	 # 查找数据
    Post = session.query(Post).filter(Post.title == '%s' % Title).one()
    data = {'time':Post.time,'context':Post.context}
    return jsonify(data)

if __name__ == '__main__':
    app.run()