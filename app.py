from flask import Flask, redirect, render_template, url_for

from flask_sqlalchemy import SQLAlchemy


local_server=True
app = Flask(__name__)
app.secret_key="sahanasaanvi"

#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@localhost/foodshare'
db=SQLAlchemy(app)

class Hotel(db.Model):
    hotelID=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30))
    email=db.Column(db.String(30))
    phone=db.Column(db.Integer)
    address=db.Column(db.String(100))
    managerName=db.Column(db.String(20))
    password=db.Column(db.String(20))



@app.route("/restLogin")
def restlogin():
    return render_template("restLogin.html") 

@app.route("/charLogin")
def charlogin():
    return render_template("charLogin.html")

@app.route("/restHome")
def restHome():
    return render_template("restHome.html")

@app.route("/charHome")
def charHome():
    return render_template("charHome.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/foodDonate")
def contact():
    return render_template("foodDonate.html")

@app.route("/test")
def test():
    try:
        a=Hotel.query.all()
        print(a)
        return "database connected"
    except Exception as e:
        return f"database not connected {e}"


app.run(debug=True)