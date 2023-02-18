from flask import Flask, request
app = Flask(__name__)


@app.route('/hi', methods=['GET','POST'])
def hello_world():
    login,passwd= request.form.get("login"),request.form.get("passwd")
    print(login,passwd)
    if login == None and passwd == None:
        return '<form action="/hi" method="post"><input type="text" name="login"><input type="password" name="passwd"><input type="submit"></form>'
    else:
        return f'<h1>{login,passwd}</h1><form action="/hi" method="post"><input type="text" name="login"><input type="password" name="passwd"><input type="submit"></form>'

app.run()
