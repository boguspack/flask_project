from flask import render_template,url_for,redirect
from app import app
from form import signupform
from loginform import loginform


@app.route("/signup",methods=['GET','POST'])
def signup():
    form = signupform()
    if form.validate_on_submit():
        fname= form.firstname.data
        lname=form.lastname.data
        email=form.email.data
        password=form.password.data
        gender=form.gender.data
        dob=form.DOB.data

        print(fname,lname,gender,email,dob,password)

        return redirect(url_for('home'))
    return render_template("signup.html", form = form)


@app.route("/login",methods=['GET','POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data

        return redirect(url_for('home'))
    return render_template("login.html", form = form)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


