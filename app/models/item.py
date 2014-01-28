from app import db
from datetime import datetime

class Item(db.Model):
  __tablename__ = 'items'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(40))
  description = db.Column(db.String(300))
  sellerID = db.Column(db.Integer, db.ForeignKey('student.id'))
  itemtype = db.Column(db.String(50))
  picture = db.Column(Photo(root="/Pile/app/Images",formats = {'big':'500 x 500'}))
  dateposted = db.Column(db.DateTime, default = db.func.now())


