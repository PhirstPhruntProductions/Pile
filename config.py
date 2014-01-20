
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#-----Config the app
SECRET_KEY = 'ppp_dev'

#-----Config Mail
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "465"
MAIL_USE_SSL = True
MAIL_USERNAME = 'yourfriendlykappas@gmail.com'
MAIL_PASSWORD = 'CampusStew18'

#-----Config Database
SQLALCHEMY_DATABASE_URI = 'mysql://achumbley:CampusStew18@localhost/dev'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#-----Config Admins
ADMINS = ['chumbleya@gmail.com', 'hreinmit@gmail.com']

#-----Config Upload folder
UPLOAD_FOLDER = os.path.realpath('./app') + '/uploads'
