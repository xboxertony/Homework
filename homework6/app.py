from flask import request, render_template, url_for, redirect , Flask,session
import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:pass@localhost:3306/website"
db = SQLAlchemy(app)


# users = {'test': {'password': 'test'}}


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/member')
def member():
    if session and session["state"] == "已登入":
        return render_template("member.html",session = session)
    else:
        return redirect(url_for('home'))


@app.route('/error/<message>')
def error(message):
    return render_template("error.html",session = session,mes = message)


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    data = user.query.filter_by(username = user_id).first()
    if not data:
        return redirect(url_for('error',message="帳號密碼輸入錯誤"))
    if request.form['password'] == data.password:
        session["realname"]=data.name
        session["user_name"] = user_id
        session["state"] = "已登入"
        # session.permanent = True
        return redirect(url_for('member'))

    return redirect(url_for('error',message="帳號密碼輸入錯誤"))


class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    time = db.Column(db.DateTime,onupdate=datetime.datetime.now,default=datetime.datetime.now)

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password

@app.route("/signup",methods=["POST"])
def signup():
    username = request.form.get("username")
    user_id = request.form.get("user_id")
    password = request.form.get("password")
    data = user.query.filter_by(username=user_id).first()
    if not username or not user_id or not password:
        return redirect(url_for("error",message="請勿輸入空值"))
    if data:
        return redirect(url_for("error",message="帳號已被註冊"))
    else:
        new_user = user(username,user_id,password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home"))



@app.route('/signout')
def logout():
    session['user_name'] = False
    session["state"] = "未登入"
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True,port=3000)