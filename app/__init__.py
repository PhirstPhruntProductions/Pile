###########################################################
# The package for the Pile Application
###########################################################

# Import statements go here

from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USE_SSL, MAIL_USERNAME, MAIL_PASSWORD, UPLOAD_FOLDER, SECRET_KEY

app = Flask(__name__)

mail = Mail()
mail.init_app(app)

db = SQLAlchemy(app)

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

