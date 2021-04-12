from flask import request, render_template, url_for, redirect , Flask,jsonify,make_response
from itsdangerous import TimedJSONWebSignatureSerializer
import datetime
from flask_sqlalchemy import SQLAlchemy
import json
# from flask_bcrypt import Bcrypt

expire_date = datetime.datetime.now()+datetime.timedelta(days=90)
# from server import app,db
# from model.user_model import user


app = Flask(__name__)
# app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:pass@localhost:3306/website"
db = SQLAlchemy(app)

# bcrypt = Bcrypt(app)

s = TimedJSONWebSignatureSerializer("abc")
check = "check"



# users = {'test': {'password': 'test'}}


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/member/')
def member():
    if "token" in request.cookies and s.loads(request.cookies.get("token"))["check"]==check:
        res = {
            "realname":s.loads(request.cookies.get("token"))["realname"],
            "state":"已登入"
        }
        return render_template("member.html",cookie = res)
    else:
        return redirect(url_for('home'))
    # if session and session["state"] == "已登入":
    #     return render_template("member.html",session = session)
    # else:
    #     return redirect(url_for('home'))


@app.route('/error/')
def error():
    message = request.args.get("message")
    return render_template("error.html",mes = message)


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    data = user.query.filter_by(username = user_id).first()
    if not data:
        return redirect('error/?message=帳號或密碼輸入錯誤')
    if request.form['password'] == data.password:
        response = make_response(redirect(url_for('member')))
        response.set_cookie(key = "token",value=s.dumps({"user_name":user_id,"realname":data.name,"check":check}).decode("utf8"),expires=expire_date)
        return response

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
    response = make_response(redirect(url_for('home')))
    response.set_cookie(key = "token",value='',expires=0)
    return response


@app.route("/api/user",methods=["GET","POST"])
def renew():
    try:
        if s.loads(request.cookies.get("token"))["check"]!=check:
            return json.dumps({
                "error":True
            })
        person = request.get_json()
        username = s.loads(request.cookies.get("token"))["user_name"]
        p = user.query.filter_by(username=username).first()
        if not person["name"]:
            return json.dumps({
                "error":True
            })
        p.name = person["name"]
        db.session.commit()
        response = jsonify({"ok":True})
        response.set_cookie(key = "token",value=s.dumps({"user_name":username,"realname":person["name"],"check":check}).decode("utf8"),expires=expire_date)
        # session["realname"]=person["name"]
        return response
    except:
        return jsonify({
            "error":True
        })


@app.route("/api/users")
def find_user():
    if "token" not in request.cookies or s.loads(request.cookies.get("token"))["check"]!=check:
        return redirect("/")
    r = request.args.get("username")
    person = user.query.filter_by(username=r).first()
    if person:
        return json.dumps({"data":{
            "id":person.id,
            "name":person.name,
            "username":person.username
        }
        },ensure_ascii=False)
    else:
        return json.dumps({
            "data":person
        })

if __name__=="__main__":
    app.run(debug=True,port=3000)