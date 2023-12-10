from flask import Flask, redirect, render_template, url_for
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy
=======
>>>>>>> f2c050cf1fd6f723fb7e9dedcc4a43cff816b855

local_server=True
app = Flask(__name__)
app.secret_key="sahanasaanvi"

<<<<<<< HEAD
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


=======
>>>>>>> f2c050cf1fd6f723fb7e9dedcc4a43cff816b855
@app.route("/")
def login():
    return render_template("login.html")

<<<<<<< HEAD
@app.route("/test")
def test():
    try:
        a=Hotel.query.all()
        print(a)
        return "database connected"
    except Exception as e:
        return f"database not connected {e}"



=======
>>>>>>> f2c050cf1fd6f723fb7e9dedcc4a43cff816b855
app.run(debug=True)