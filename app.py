from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app= Flask(__name__)

app.config["SECRET_KEY"] ="cd4efa1159263e7118e076584d317ec0"
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///site.db"

db=SQLAlchemy(app)
bcrypt= Bcrypt(app)
loginM= LoginManager(app)

loginM.login_view= "login"
loginM.login_message_category= "info"

from  routes import *

if __name__ == '__main__':
    app.run(debug=True)