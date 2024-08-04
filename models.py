from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=False, nullable=False)
    lname = db.Column(db.String(15), unique=False, nullable=False)
    pwd = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"user({self.fname},{self.email})"
