from db import db

class UserModel(db.Model):
    __tablename__ = "Users"

    id = db.Coulmn(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
    