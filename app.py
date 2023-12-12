from flask import Flask, redirect, render_template, url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_required,logout_user,login_user,login_manager,LoginManager,current_user
import uuid,json
from datetime import datetime


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
    return hotel.query.get(user_id) or charity.query.get(user_id)



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
def index():
    return render_template("index.html")

@app.route("/restLogin")
def restLogin():
    return render_template("restLogin.html")

@app.route("/charLogin")
def charLogin():
    return render_template("charLogin.html")



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

        user=hotel.query.filter_by(email=email).first()
        if user:
            #flash("Email is already taken","warning")
            return render_template("restLogin.html")

        #print(hotelID,name,email,passwd,phone,address,manager)
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

        #login_user(user)

        #flash("SignUp Success","success")
        return render_template("restHome.html")
    return render_template("restLogin.html")

@app.route("/restsignin", methods=['POST','GET'])
def restsignin():
    if request.method == 'POST':
        email=request.form.get('email')
        passwd=request.form.get('passwd')

        user=hotel.query.filter_by(email=email, passwd=passwd).first()

        if user:
            #login_user(user)
            #flash("Login Success","info")
            return render_template("restHome.html")
        else:
            #flash("Invalid Credentials","danger")
            return render_template('restLogin.html')
    return render_template('restLogin.html')
    


@app.route("/charsignup", methods=['POST','GET'])
def charsignup():
    if request.method == 'POST':
        charityID = str(uuid.uuid4())[:8]
        name=request.form.get('name')
        email=request.form.get('email')
        passwd=request.form.get('passwd')
        phone=str(request.form.get('phone'))
        address=request.form.get('address')
        manager=request.form.get('manager')

        emailUser=charity.query.filter_by(email=email).first()
        if emailUser:
            #flash("Email is already taken","warning")
            return render_template("restLogin.html")

        #print(charityID,name,email,passwd,phone,address,manager)
        new_charity = charity(
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

        remove_expired_food()

        #flash("SignUp Success","success")
        return render_template("charHome.html")
    return render_template("charLogin.html")

@app.route("/charsignin", methods=['POST','GET'])
def charsignin():
    if request.method == 'POST':
        email=request.form.get('email')
        passwd=request.form.get('passwd')

        user=charity.query.filter_by(email=email, passwd=passwd).first()

        if user:
            remove_expired_food()
            #login_user(user)
            #flash("Login Success","info")
            return render_template("charHome.html")
        else:
            #flash("Invalid Credentials","danger")
            return render_template('charLogin.html')
    return render_template('charLogin.html')

    
def remove_expired_food():
    current_date = datetime.now()
    expired_food = food.query.filter(food.expiry == current_date).all()

    for item in expired_food:
        db.session.delete(item)
    db.session.commit()




@app.route("/foodDonate", methods=['POST','GET'])
def foodDonate():
    if request.method == 'POST':
        foodID = str(uuid.uuid4())[:8]
        name=request.form.get('name')
        qty=request.form.get('qty')
        type=request.form.get('type')

        current_date = datetime.now()
        date = current_date.strftime("%d/%m/%y")

        expiry=request.form.get('expiry')
        description=request.form.get('description')
        print(name,qty,type,date,expiry,description)

        new_food = food(
            foodID=foodID,
            name=name,
            qty=qty,
            type=type,
            date=date,
            expiry=expiry,
            description=description,
        )
        
        db.session.add(new_food)
        db.session.commit()

        return render_template("foodDonate.html")
    return render_template("foodDonate.html")



@app.route("/charContact")
def charContact():
    return render_template("charContact.html")

@app.route("/restContact")
def restContact():
    return render_template("restContact.html")

@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/restHome")
def restHome():
    return render_template("restHome.html")

@app.route("/restProfile")
def restProfile():
    return render_template("restProfile.html")



@app.route("/charHome")
def charHome():
    return render_template("charHome.html")

@app.route("/charProfile")
def charProfile():
    return render_template("charProfile.html")



@app.route('/charLogout')
#@login_required
def charLogout():
    logout_user()
    return render_template("charLogin.html")

@app.route('/restLogout')
#@login_required
def restLogout():
    logout_user()
    return render_template("restLogin.html")


app.run(debug=True)