from datetime import datetime
from flask import Flask,render_template,redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    profilePicture = db.Column(db.LargeBinary)
    username = db.Column(db.String(100),nullable=False)
    createdAt= db.Column(db.DateTime,default=datetime.utcnow) 
    updatedAt= db.Column(db.DateTime,default=datetime.utcnow) 
    def __repr__(self):
        return f"User {self.id}"
    
class Messages(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    senderId=db.Column(db.Integer,foreign_key=True)
    receiverId=db.Column(db.Intege, foreign_key=True)
    content=db.Column(db.String(10000000),nullable=False)
    createdAt= db.Column(db.DateTime,default=datetime.utcnow) 
    updatedAt= db.Column(db.DateTime,default=datetime.utcnow) 
    def __repr__(self):
        return f"Messages {self.id}"
    

class Friends(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    friendSince=db.Column(db.DateTime,default=datetime.utcnow)

