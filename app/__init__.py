###########################################################
# The package for the Pile Application
###########################################################

# Import statements go here

from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#-----Config the app
app.secret_key = 'ppp_dev'

#-----Config Mail
mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = "465"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'yourfriendlykappas@gmail.com'
app.config['MAIL_PASSWORD'] = 'CampusStew18'
mail.init_app(app)

#-----Config Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://achumbley:CampusStew18@localhost/dev'
app.config['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')
db = SQLAlchemy(app)

#-----Config Upload folder
app.config['UPLOAD_FOLDER'] = os.path.realpath('./app') + '/uploads'

#-----URL Routes for website
from app.views import *

#-----Models form DB
from models.user import *
from models.college import *
from models.item import *

#-----API Support
from api.users import *
from api.colleges import *
from api.items import *

