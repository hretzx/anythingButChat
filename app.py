from flask import Flask,render_template,redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False

db=SQLAlchemy(app)

