from pile import db
from datetime import datetime
from pile.custom_db.GUID import GUID
import uuid

item_types = ('Electronics', 'Books', 'Clothing', 'Dorm Items', 'Miscellaneous')
class Item(db.Model):
  __tablename__ = 'items'
  id = db.Column(db.Integer(), primary_key=True)
  public_id = db.Column(GUID(), unique=True, default=uuid.uuid4())
  name = db.Column(db.String(40))
  description = db.Column(db.String(300))
  contact_info = db.Column(db.String(300))
  price = db.Column(db.Integer)
  user_id = db.Column(GUID(), db.ForeignKey('users.public_id'))
  college_id = db.Column(GUID(), db.ForeignKey('colleges.public_id'))
  item_type = db.Column(db.Enum(*item_types))
  #image = db.Column(Photo(root="/Pile/app/Images",formats = {'big':'500 x 500'}))
  date_posted = db.Column(db.DateTime, default = db.func.now())

  def __init__(self, name, description, contact_info, price, user_id, college,_id, item_type):#, image):
    self.name = name
    self.description = description
    self.contact_info = contact_info
    self.price = price
    self.user_id = user_id
    self.college_id = college_id
    self.item_type = item_type
    #self.image = image

  def __repr__(self):
    return '<Item %r>' % self.name


