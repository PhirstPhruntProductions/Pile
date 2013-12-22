#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from app import app


#------------------------------------------------

api = Api(app)

user_fields = {

}

def userExists(id):
  pass

def getUser(id):
  pass

def addUser(user):
  pass

def updateUser(**kwargs):
  pass

def deleteUser(id):
  pass

def getAllUsersByCollege(college):
  pass

class UserAPI(Resource):
  def __init__(self):
    pass

  def get(self, id):
    pass

  def put(self, id):
    pass

  def delete(self, id):
    pass

api.add_resource(UserAPI, '/api/user/<int:id>', endpoint = 'user')

class UserListAPI(Resource):
  def __init__(self):
    pass

  def get(self):
    pass

  def post(self):
    pass

api.add_resource(UserListAPI, '/api/users/', endpoint = 'users')

class UsersByCollegeAPI(Resource):
  def _init__(self):
    pass

  def get(self, id):
    pass

api.add_resource(UsersByCollegeAPI, '/api/college/<int:id>/users', endpoint = 'users_by_college')



