from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "test"

@app.errorhandler(404)
def error(_=None):
    return "omg"#redirect("https://www.youtube.com/watch?v=q-Y0bnx6Ndw")