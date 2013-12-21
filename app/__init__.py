from flask import Flask

app = Flask(__name__)

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
