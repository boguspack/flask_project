from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config["SECRET_KEY"] ="cd4efa1159263e7118e076584d317ec0"


from  routes import *
