from flask import request, render_template, url_for, redirect , Flask,session
from datetime import timedelta
from flask_bcrypt import Bcrypt

# binascii.hexlify(os.urandom(16)).decode()


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'
app.permanent_session_lifetime = timedelta(days=3)
bcrypt = Bcrypt(app)
p_hash = bcrypt.generate_password_hash('ttoooott').decode('utf-8')
# print(p_hash)
# print(bcrypt.check_password_hash(p_hash,"ttoooott"))


users = {'test': {'password': 'test'}}


@app.before_request
def login_required():
    if request.path in ["","/","/signin","/signout","/error","/static"]:
        return None
    print(session)
    user = session.get("user_name")

    if user==False or not user:
        print(request.path)
        return redirect("/")


@app.route('/')
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
        return render_template("error.html",session = session)
    else:
        return redirect(url_for("home"))


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    if (user_id in users) and (request.form['password'] == users[user_id]['password']):
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