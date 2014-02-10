from pile import db
from pile.custom_db.GUID import GUID
import uuid

class College(db.Model):
  __tablename__ = 'colleges'
  id = db.Column(GUID(), primary_key=True, default=uuid.uuid4())
  name = db.Column(db.String(40), unique = True)
  email_stub = db.Column(db.String(30), unique = True)
  num_users = db.Column(db.Integer)
		
  def __init__(self, name, email_stub):
    self.name = name
    self.email_stub = email_stub
    self.num_users = 0

  def __repr__(self):
    return '<College %r>' % self.name
