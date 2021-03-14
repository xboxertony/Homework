from flask import request, render_template, url_for, redirect, flash, Flask,session
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'


users = {'test': {'password': 'test'}}

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(user_id):
    if user_id not in users:
        return
    
    user = User()
    user.id = user_id
    return user

@login_manager.request_loader
def request_loader(request):
    user_id = request.form.get('user_id')
    if user_id not in users:
        return
    
    if user_id in users and request.form['password'] != users[user_id]['password']:
        return

    user = User()
    user.id = user_id

    user.is_authenticated = True
    return user


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/member')
def member():
    if session and session["state"] == "已登入":
        return render_template("member.html")
    else:
        return redirect(url_for('home'))


@app.route('/error')
def error():
    return render_template("error.html")


@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    if (user_id in users) and (request.form['password'] == users[user_id]['password']):
        user = User()
        user.id = user_id
        login_user(user)
        session["user_name"] = user_id
        session["state"] = "已登入"
        print(session)
        return redirect(url_for('member'))

    return redirect(url_for('error'))



@app.route('/signout', methods=['GET', 'POST'])
def logout():
    logout_user()
    session["state"] = "未登入"
    print(session)
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True)