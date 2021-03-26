from flask import request, render_template, url_for, redirect , Flask,session
from datetime import timedelta
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# binascii.hexlify(os.urandom(16)).decode()


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'
app.permanent_session_lifetime = timedelta(days=3)
bcrypt = Bcrypt(app)
p_hash = bcrypt.generate_password_hash('ttoooott').decode('utf-8')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost:3306/test2'
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(100))

    def __init__(self,name,password):
        self.username = name
        self.password = password

db.create_all()
# print(p_hash)
# print(bcrypt.check_password_hash(p_hash,"ttoooott"))


# users = {'test': {'password': 'test'}}


@app.before_request
def login_required():
    if request.path in ["","/","/signin","/signout","/error","/static","/signup","/favicon.ico","/sign"]:
        print(2222)
        return None
    print(11111)
    user = session.get("user_name")

    if user==False or not user:
        print(request.path)
        return redirect("/")

@app.route('/',methods=["GET","POST"])
def signup():
    if request.method=="POST":
        session["username"]=request.form["username"]
        session["password"]=bcrypt.generate_password_hash(request.form["password"]).decode("utf8")
        return redirect(url_for("signup_f"))
    return render_template("signup.html")


@app.route("/signup")
def signup_f():
    # print(bcrypt.check_password_hash(session["password"],"1111"))
    p = user(session["username"],session["password"])
    db.session.add(p)
    db.session.commit()
    session["username"]=False
    session["password"]=False
    return "ok"


@app.route('/sign')
def home():
    user = session.get("user_name")
    return render_template("login.html",user = user)

@app.route('/member')
def member():
    # print("from member:")
    # print(session)
    # if session and session["state"] == "已登入":
    return render_template("member.html",session = session)
    # else:
    #     return redirect(url_for('home'))


@app.route('/error')
def error():
    if not session.get("user_name",""):
        if "error" not in session:
            session["error"]=1
        else:
            session["error"]+=1
        return render_template("error.html",session = session)
    else:
        return redirect(url_for("home"))


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    users = {p.username:p.password for p in user.query.all()}
    if (user_id in users) and (bcrypt.check_password_hash(users[user_id],str(request.form['password']))):
        session.permanent = True
        session["user_name"] = user_id
        session["state"] = "已登入"
        return redirect(url_for('member'))

    return redirect(url_for('error'))



@app.route('/signout')
def logout():
    session['user_name'] = False
    session["state"] = "未登入"
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True,port=3000)