#------------------------------------------------
#Imports go here
from flask import jsonify, abort, request, make_response, url_for, g, flash, redirect, render_template
from flask.ext.restful import Api, Resource, reqparse, fields, marshal, marshal_with
from app import app


#------------------------------------------------

api = Api(app)

def itemExists(id):
  if Item.query.filter_by(id=id).first():
    return True
  return False

def getItem(id):
  return Item.query.filter_by(id=id).first()

def addItem(item):
  db.session.add(item)
  db.session.commit()

def updateItem(**kwargs):
  pass

def deleteItem(id):
  item = Item.query.filter_by(id=id).first():
  db.session.add(item)
  db.session.commit()

def getAllItemsByCollege(college):
  return Item.query.filter_by(college=college).all()

def getAllItemsByUser(user):
  return Item.query.filter_by(user=user).all()

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

items_by_type_fields = {

}

class ItemsByTypeAPI(Resource):
  def __init__(self):
    pass

  def get(self, type):
    pass

api.add_resource(ItemsByTypeAPI, '/api/<string:type>/items', endpoint = 'items_by_type')

items_by_search_fields = {

}

class ItemsByTextSearchAPI(Resource):
  def __init__(self):
    pass

  def get(self, text):
    pass

api.add_resource(ItemsByTypeAPI, '/api/items/search/<string:text>', endpoint = 'items_by_search')



