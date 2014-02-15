from pile import db
from datetime import datetime
from pile.custom_db.GUID import GUID
import uuid

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer(), primary_key=True)
  public_id = db.Column(GUID(), unique=True, default=uuid.uuid4())
  email = db.Column(db.String(80), unique=True)
  name = db.Column(db.String(80))
  password = db.Column(db.String(80))
  college_id = db.Column(GUID() ,db.ForeignKey('colleges.public_id'))
  datejoined = db.Column(db.DateTime,default = db.func.now())

  def __init__(self, name, email, password, college):
    self.name = name
    self.email = email
    self.password = password
    self.college = college

  def __repr__(self):
    return '<User %r>' % self.name


  



