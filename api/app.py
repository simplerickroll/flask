from flask import Flask, redirect
app = Flask(__name__)

@app.errorhandler(404)
def error(_=None):
    return redirect("https://www.youtube.com/watch?v=q-Y0bnx6Ndw")