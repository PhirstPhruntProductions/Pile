#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from app import app


#------------------------------------------------

api = Api(app)

colege_fields = {

}

def collegeExists(id):
  pass

def getCollege(id):
  pass

def addCollege(user):
  pass

def updateCollege(**kwargs):
  pass

def deleteCollege(id):
  pass

def getAllColleges():
  pass

class CollegeAPI(Resource):
  def __init__(self):
    pass

  def get(self, id):
    pass

  def put(self, id):
    pass

  def delete(self, id):
    pass

api.add_resource(CollegeAPI, '/api/college/<int:id>', endpoint = 'college')

class CollegeListAPI(Resource):
  def __init__(self):
    pass

  def get(self):
    pass

  def post(self):
    pass

api.add_resource(CollegeListAPI, '/api/colleges/', endpoint = 'colleges')

#Potentially unnecessary
class CollegeByNameAPI(Resource):
  def __init__(self):
    pass

  def get(self, id):
    pass

api.add_resource(CollegeByNameAPI, '/api/college_by_name/<string:name>', endpoint = 'college_by_name')


