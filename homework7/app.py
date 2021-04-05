from flask import request, render_template, url_for, redirect , Flask,session
import datetime
from flask_sqlalchemy import SQLAlchemy
import json
# from server import app,db
# from model.user_model import user


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:pass@localhost:3306/website"
db = SQLAlchemy(app)


# users = {'test': {'password': 'test'}}


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/member/')
def member():
    if session and session["state"] == "已登入":
        return render_template("member.html",session = session)
    else:
        return redirect(url_for('home'))


@app.route('/error/')
def error():
    message = request.args.get("message")
    return render_template("error.html",session = session,mes = message)


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    data = user.query.filter_by(username = user_id).first()
    if not data:
        return redirect('error/?message=帳號或密碼輸入錯誤')
    if request.form['password'] == data.password:
        session["realname"]=data.name
        session["user_name"] = user_id
        session["state"] = "已登入"
        # session.permanent = True
        return redirect(url_for('member'))

    return redirect('error/?message=帳號或密碼輸入錯誤')


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
        return redirect("error/?message=請勿輸入空值")
    if data:
        return redirect("error/?message=帳號已經被註冊")
    new_user = user(username,user_id,password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("home"))



@app.route('/signout')
def logout():
    session['user_name'] = False
    session["state"] = "未登入"
    return redirect(url_for("home"))


@app.route("/api/user",methods=["POST"])
def renew():
    try:
        person = request.get_json()
        p = user.query.filter_by(username=session["user_name"]).first()
        if not person["name"]:
            return json.dumps({
                "error":True
            })
        p.name = person["name"]
        db.session.commit()
        session["realname"]=person["name"]
        return json.dumps({
            "ok":True
        })
    except:
        return json.dumps({
            "error":True
        })


@app.route("/api/users")
def find_user():
    if "state" not in session or session["state"]=="未登入":
        return redirect("/")
    r = request.args.get("username")
    person = user.query.filter_by(username=r).first()
    if person:
        return json.dumps({"data":{
            "id":person.id,
            "name":person.name,
            "username":person.username
        }
        })
    else:
        return json.dumps({
            "data":person
        })

if __name__=="__main__":
    app.run(debug=True,port=3000)