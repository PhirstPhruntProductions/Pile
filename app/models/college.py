from app import db

class College(db.Model):
  __tablename__ = 'colleges'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(40), unique = True)
  emailstub = db.Column(db.String(30), unique = True)
  numUsers = db.Column(db.Integer)
  students = db.relationship('Student',backref = 'college',lazy = 'dynamic')
  verified = db.Column(db.Boolean)
		
  def __init__(self, name, emailstub):
    self.name = name
    self.emailstub = emailstub
    self.numUsers = 0
    self.verified = False

  def __repr__(self):
    return '<College %r>' % self.name
