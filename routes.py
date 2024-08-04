from flask import render_template, url_for, redirect
from app import app, db
from form import signupform, loginform
from models import User


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = signupform()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        gender = form.gender.data
        dob = form.DOB.data

        person = User(
            fname=firstname,
            lname=lastname,
            email=email,
            pwd=password,
            gender=gender,
            dob=dob,
        )

        print(person)

        db.session.add(person)
        db.session.commit()
        del person

        return redirect(url_for("home"))
    return render_template("signup.html", form=form) 


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
