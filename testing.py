from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/register" , methods=["POST","GET"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template('index.html', username=username, password=password)