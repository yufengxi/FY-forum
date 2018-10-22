from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
	
@app.route('/signin', methods=['GET', 'POST'])
def signin_form():
    return render_template('form.html')

@app.route('/sign', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='feiyang' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()
