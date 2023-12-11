from flask import Flask, redirect, render_template, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required,logout_user,login_user,login_manager,LoginManager,current_user
import uuid
from werkzeug.security import generate_password_hash,check_password_hash

local_server=True
app = Flask(__name__)
app.secret_key="sahanasaanvi"

login_manager=LoginManager(app)
login_manager.login_view='login'

#app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql://root:@localhost/foodshare'
db=SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    hotel_user = hotel.query.get(user_id)
    if hotel_user:
        return hotel_user
    
    charity_user = charity.query.get(user_id)
    if charity_user:
        return charity_user
    
    return None

class hotel(db.Model):
    hotelID=db.Column(db.String(8),primary_key=True)
    name=db.Column(db.String(30))
    email=db.Column(db.String(20), unique=True)
    passwd=db.Column(db.String(20), unique=True)
    phone=db.Column(db.String(10))
    address=db.Column(db.String(100))
    manager=db.Column(db.String(20))

class charity(db.Model):
    charityID=db.Column(db.String(8),primary_key=True)
    name=db.Column(db.String(30))
    email=db.Column(db.String(20), unique=True)
    passwd=db.Column(db.String(20), unique=True)
    phone=db.Column(db.String(10))
    address=db.Column(db.String(100))
    manager=db.Column(db.String(20))

class food(db.Model):
    foodID=db.Column(db.String(8),primary_key=True)
    name=db.Column(db.String(20))
    qty=db.Column(db.Integer)
    type=db.Column(db.String(7))
    date=db.Column(db.Date)
    expiry=db.Column(db.Date)
    description=db.Column(db.String(50))
    
class donate(db.Model):
    foodID=db.Column(db.String(8),primary_key=True)
    hotelID=db.Column(db.String(8),primary_key=True)

class accept(db.Model):
    foodID=db.Column(db.String(8),primary_key=True)
    charityID=db.Column(db.String(8),primary_key=True)


@app.route("/")
def login():
    return render_template("restLogin.html")

@app.route("/restsignup", methods=['POST','GET'])
def restsignup():
    if request.method == 'POST':
        hotelID = str(uuid.uuid4())[:8]
        name=request.form.get('name')
        email=request.form.get('email')
        passwd=request.form.get('passwd')
        phone=str(request.form.get('phone'))
        address=request.form.get('address')
        manager=request.form.get('manager')

        print(hotelID,name,email,passwd,phone,address,manager)
        new_hotel = hotel(
            hotelID=hotelID,
            name=name,
            email=email,
            passwd=passwd,
            phone=phone,
            address=address,
            manager=manager
        )
        
        db.session.add(new_hotel)
        db.session.commit()

        return render_template("restHome.html")
    return render_template("restLogin.html")

@app.route("/restsignin", methods=['POST','GET'])
def restsignin():
    if request.method == 'POST':
        email=request.form.get('email')
        passwd=request.form.get('passwd')
        print(email,passwd)
        return render_template("restHome.html")
    

@app.route("/charsignup", methods=['POST','GET'])
def charsignup():
    if request.method == 'POST':
        charityID = str(uuid.uuid4())[:8]
        name=request.form.get('name')
        email=request.form.get('email')
        passwd=request.form.get('passwd')
        phone=request.form.get('phone')
        address=request.form.get('address')
        manager=request.form.get('manager')
        print(charityID,name,email,passwd,phone,address,manager)
        
        new_charity= charity(
            charityID=charityID,
            name=name,
            email=email,
            passwd=passwd,
            phone=phone,
            address=address,
            manager=manager
        )
        
        db.session.add(new_charity)
        db.session.commit()

        return render_template("charHome.html")
    return render_template("charLogin.html")

@app.route("/charsignin", methods=['POST','GET'])
def charsignin():
    if request.method == 'POST':
        email=request.form.get('email')
        passwd=request.form.get('passwd')
        print(email,passwd)
        return render_template("charHome.html")



@app.route("/restHome")
def restHome():
    return render_template("restHome.html")

@app.route("/charHome")
def charHome():
    return render_template("charHome.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/restProfile")
def restProfile():
    return render_template("restProfile.html")

@app.route("/charProfile")
def charProfile():
    return render_template("charProfile.html")

@app.route("/foodDonate")
def foodDonate():
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