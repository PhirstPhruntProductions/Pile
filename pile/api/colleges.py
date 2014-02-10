#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from pile import app
from pile.models.college import *

#------------------------------------------------

api = Api(app)


def collegeExists(id):
  if College.query.filter_by(id=id).first():
    return True
  return False

def getCollege(id):
  return College.query.filter_by(id=id).first()

def addCollege(college):
  db.session.add(college)
  db.session.commit()

def updateCollege(**kwargs):
  pass

def deleteCollege(id):
  college = College.query.filter_by(id=id).first()
  db.session.delete(college)
  db.session.commit()

def getAllColleges():
  return College.query.all()

college_fields = {
  'name': fields.String,
  'email_stub': fields.String,
  'num_users': fields.Integer
}

class CollegeAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('email_stub', type = str, required = True, help = "No email_stub provided", location = 'json')
    super(CollegeAPI, self).__init__()

  def get(self, id):
    if collegeExists(id):
      return { 'college':marshal(getCollege(id), college_fields) }
    abort(404)

  def put(self, id):
    if collegeExists(id):
      args = self.reqparse.parse_args()
      deleteCollege(id)
      college = College(args['name'], args['email_stub'])
      addCollege(college)
      return {'college' : marshal(college, college_fields)}, 201
    abort(404)

  def delete(self, id):
    deleteCollege(id)
    return {'result': True}

api.add_resource(CollegeAPI, '/api/college/<int:id>', endpoint = 'college')

class CollegeListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('email_stub', type = str, required = True, help = "No email_stub provided", location = 'json')
    super(CollegeListAPI, self).__init__()

  def get(self):
    return { 'colleges': map(lambda t: marshal(c, college_fields), getAllColleges()) }

  def post(self):
    args = self.reqparse.parse_args()
    new_college = College(args['name'], args['email_stub'])
    addCollege(new_college)
    return {'college' : marshal(new_college, college_fields)}, 201

api.add_resource(CollegeListAPI, '/api/colleges/', endpoint = 'colleges')

