from flask import Flask, redirect
app = Flask(__name__)

@app.errorhandler(404)
def index(_=None):
    return "omg"#redirect("https://www.youtube.com/watch?v=q-Y0bnx6Ndw")