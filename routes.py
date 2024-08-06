from flask import render_template, url_for, redirect, flash
from app import app, db , bcrypt
from form import signupform, loginform
from models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated: 
        return redirect(url_for("about"))
    
    form = signupform()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        gender = form.gender.data
        dob = form.DOB.data

        hashpassword=bcrypt.generate_password_hash(password).decode("utf-8")

        person = User(
            fname=firstname,
            lname=lastname,
            email=email,
            pwd=hashpassword,
            gender=gender,
            dob=dob,
        )

        print(person)

        db.session.add(person)
        db.session.commit()

        flash("Account created","success")


        del person

        return redirect(url_for("login"))
    return render_template("signup.html", form=form) 


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for("about"))
    form = loginform()
    if form.validate_on_submit():
        user= User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.pwd,form.password.data):
            login_user(user)
            return redirect(url_for("about"))
        else:
            flash("login unsuccessful","danger")
    return render_template("login.html", form=form)


@app.route('/about')
@login_required
def about():
    return render_template("about.html")



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))





