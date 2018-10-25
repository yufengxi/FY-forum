from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def default():
    return render_template('home.html')
	
@app.route('/home', methods=['GET','POST'])
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
    # 需要从request对象读取表单内容,flask通过requst.form['name']来获取表单的内容
    username = request.form['username']
    password = request.form['password']
    # 连接数据库
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/User')
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 查找数据
    try:
        user = session.query(User).filter(User.name=='%s' % username).one()
    except Exception as e:
        session.close()
        return render_template('login.html', message='用户不存在，请检查后再输入！', username=username)
    # 关闭
    session.close()
    if password != user.password:
        return render_template('login.html', message='密码错误，请检查后再输入！', username=username)
    return render_template('home.html', username=username)
	
@app.route('/register', methods=['POST'])
def register(name=None):
    username = request.form['username']
    password = request.form['password']
    re_password = request.form['re_password']
    # 建立连接，数据库
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/User')
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    # 查找数据
    user = session.query(User).filter(User.name=='%s' % username).one()
    if username == user.name:
        return render_template('register.html', message='用户名已存在，请直接登录！', username=username)
    elif password != re_password:
        return render_template('register.html', message='两次输入的密码不一致，请检查后重新输入！', username=username)
    elif not username or not password:
        return render_template('register.html', message='用户名和密码不能为空，请检查后重新输入！', username=username)
    # 数据没问题，则存储到数据库dtt_web
    # 插入数据
    new_user = User(username='%s', password='%s' %(username, password))
    session.add(new_user)
    # 提交事务
    session.commit()
    # 关闭游标和连接
    session.close()
    return render_template('register.html')

@app.route('/notice', methods=['GET'])
def notice():
    return render_template('notice.html')
	
@app.route('/post', methods=['GET'])
def post():
    return render_template('post.html')
	
if __name__=='__main__':
    # 若不配置host和port，则默认是localhost，端口为5000
    # 若配置，如写作app.run("",8000)，就是localhost，端口8000
    app.run()