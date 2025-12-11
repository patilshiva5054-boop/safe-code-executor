from flask import Flask, send_from_directory

@app.route("/")
def index():
    return send_from_directory("web", "index.html")
