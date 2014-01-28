from app import db
from datetime import datetime

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  college = db.Column(db.Integer,db.ForeignKey('college.id'))
  items = db.relationship('Item',backref = 'seller', lazy = 'dynamic')	
  datejoined = db.Column(db.DateTime,default = db.func.now())
  age = db.Column(db.Integer)

  def __init__(self, username,name,college):
    self.username = username
    self.name = name
    self.college = college #MIGHT NEED TO DO MORE THAN THIS TO INITIALIZE

  def __repr__(self):
    return #Put some string here


  



