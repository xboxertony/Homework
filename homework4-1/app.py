from flask import request, render_template, url_for, redirect , Flask,session


app = Flask(__name__)
app.secret_key = '26adfff637e8343fd8d2a11a32ff454c'


users = {'test': {'password': 'test'}}


@app.route('/')
def home():
    return render_template("login.html")

@app.route('/member')
def member():
    print("from member:")
    print(session)
    if session and session["state"] == "已登入":
        return render_template("member.html",session = session)
    else:
        return redirect(url_for('home'))


@app.route('/error')
def error():
    return render_template("error.html",session = session)


@app.route('/signin', methods=['POST'])
def login():
    # if request.method == 'GET':
    #     return redirect(url_for('home'))
    
    user_id = request.form['user_id']
    if (user_id in users) and (request.form['password'] == users[user_id]['password']):
        session["user_name"] = user_id
        session["state"] = "已登入"
        # session.permanent = True
        return redirect(url_for('member'))

    return redirect(url_for('error'))



@app.route('/signout')
def logout():
    session['user_name'] = False
    session["state"] = "未登入"
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True,port=3000)