#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from app import app, db


#------------------------------------------------

api = Api(app)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def userExists(id):
  if User.query.filter_by(id=id).first():
    return True
  return False

def getUser(id):
  return User.query.filter_by(id=id).first()

def addUser(user):
  db.session.add(user)
  db.session.commit()

def updateUser(**kwargs):
  pass

def deleteUser(id):
  user = User.query.filter_by(id=id).first()
  db.session.delete(user)
  db.session.commit()

def getAllUsers():
  return User.query.all()

def getAllUsersByCollege(college):
  return User.query.filter_by(college=college).all()

user_fields = {
  'username': fields.String,
  'name': fields.String,
  'college': fields.String,
}

class UserAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('username', type = str, required = True, help = "No username provided", location = 'json')
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('college', type = str, required = True, help = "No college provided", location = 'json')
    super(UserAPI, self).__init__()

  def get(self, id):
    if userExists(id):
      return { 'user':marshal(getUser(id), user_fields) }
    abort(404)

  def put(self, id):
    if userExists(id):
      args = self.reqparse.parse_args()
      deleteUser(id)
      user = User(args['username'], args['name'], args['college'])
      addUser(user)
      return {'user' : marshal(user, user_fields)}, 201
    abort(404)

  def delete(self, id):
    deleteUser(id)
    return {'result': True}

api.add_resource(UserAPI, '/api/user/<int:id>', endpoint = 'user')

class UserListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('username', type = str, required = True, help = "No username provided", location = 'json')
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('college', type = str, required = True, help = "No college provided", location = 'json')
    super(UserListAPI, self).__init__()

  def get(self):
    return { 'users': map(lambda t: marshal(u, user_fields), getAllUsers()) }

  def post(self):
    args = self.reqparse.parse_args()
    new_user = User(args['username'], args['name'], args['college'])
    addUser(new_user)
    return {'user' : marshal(new_user, user_fields)}, 201

api.add_resource(UserListAPI, '/api/users/', endpoint = 'users')

users_by_college_fields = {

}

class UsersByCollegeAPI(Resource):
  def _init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('username', type = str, required = True, help = "No username provided", location = 'json')
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('college', type = str, required = True, help = "No college provided", location = 'json')
    super(UsersByCollegeAPI, self).__init__()

  def get(self, id):
    return { 'users': map(lambda t: marshal(u, user_fields), getAllUsersByCollege()) }

api.add_resource(UsersByCollegeAPI, '/api/college/<int:id>/users', endpoint = 'users_by_college')



