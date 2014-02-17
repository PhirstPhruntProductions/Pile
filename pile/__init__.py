###########################################################
# The package for the Pile Application
###########################################################

# Import statements go here

from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

mail = Mail()
mail.init_app(app)

db = SQLAlchemy(app)

#-----URL Routes for website
from pile.views import *

#-----Models form DB
from models import user
from models.college import *
from models.item import *

#-----API Support
from api.users import *
from api.colleges import *
from api.items import *

db.create_all()

if __name__=='__main__':
  app.run()

