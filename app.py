from flask import Flask, redirect, render_template, url_for

local_server=True
app = Flask(__name__)
app.secret_key="sahanasaanvi"

@app.route("/")
def login():
    return render_template("login.html")

app.run(debug=True)