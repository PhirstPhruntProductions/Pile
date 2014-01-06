from flask import render_template
from app import app

@app.route('/')
@app.route('/index/')
def index():
  return render_template('index.html')


@app.route('/upload/')
def upload():
  return render_template('upload.html')

@app.route('/dbView/')
def dbView():
  return render_template('dbView.html')

