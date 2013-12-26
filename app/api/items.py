#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from app import app


#------------------------------------------------

api = Api(app)

def itemExists(id):
  pass

def getItem(id):
  pass

def addItem(user):
  pass

def updateItem(**kwargs):
  pass

def deleteItem(id):
  pass

def getAllItemsByCollege(college):
  pass

def getAllItemsByUser(user):
  pass

item_fields = {

}

class ItemAPI(Resource):
  def __init__(self):
    pass

  def get(self, id):
    pass

  def put(self, id):
    pass

  def delete(self, id):
    pass

api.add_resource(ItemAPI, '/api/item/<int:id>', endpoint = 'item')

items_fields = {

}

class ItemListAPI(Resource):
  def __init__(self):
    pass

  def get(self):
    pass

  def post(self):
    pass

api.add_resource(ItemListAPI, '/api/items/', endpoint = 'items')

items_by_college_fields = {

}

class ItemsByCollegeAPI(Resource):
  def _init__(self):
    pass

  def get(self, id):
    pass

api.add_resource(ItemsByCollegeAPI, '/api/college/<int:id>/items', endpoint = 'items_by_college')

items_by_user_fields = {

}

class ItemsByUserAPI(Resource):
  def __init__(self):
    pass

  def get(self, id):
    pass

api.add_resource(ItemsByUserAPI, '/api/user/<int:id>/items', endpoint = 'items_by_user')



