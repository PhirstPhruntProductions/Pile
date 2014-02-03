from flask import render_template
from app import app
import MySQLdb

def getUserData():
  db = MySQLdb.connect(host="localhost",
                     user="achumbley",
                      passwd="CampusStew18",
                      db="dev")
  cur = db.cursor() 
  cur.execute("SELECT * FROM users")

  for row in cur.fetchall() :
    print row[0]
  

@app.route('/')
@app.route('/index/')
def index():
  print getUserData
  return render_template('index.html')


@app.route('/upload/')
def upload():
  return render_template('upload.html')

@app.route('/dbView/')
def dbView():
  return render_template('dbView.html')

