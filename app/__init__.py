from flask import Flask

app = Flask(__name__)

from app.views import *
from app.models import *
from app.api import *
