from flask import Flask
from flask.ext.mail import Mail

app = Flask(__name__)

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
