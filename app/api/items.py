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
  item = Item.query.filter_by(id=id).first()
  db.session.add(item)
  db.session.commit()

def getAllItemsByCollege(college):
  return Item.query.filter_by(college=college).all()

def getAllItemsByUser(user):
  return Item.query.filter_by(user=user).all()

item_fields = {
  'name': fields.String,
  'description': fields.String,
  'contact_info': fields.String,
  'price': fields.Integer, 
  'user_id': fields.String,
  'college_id': fields.String,
  'item_type': fields.String,
}

class ItemAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('description', type = str, required = True, help = "No description provided", location = 'json')
    self.reqparse.add_argument('contact_info', type = str, required = True, help = "No contact_info provided", location = 'json')
    self.reqparse.add_argument('price', type = int, required = True, help = "No price provided", location = 'json')
    self.reqparse.add_argument('item_type', type = str, required = True, help = "No item_type provided", location = 'json')
    self.reqparse.add_argument('user_id', type = str, required = True, help = "No user_id provided", location = 'json')
    super(ItemAPI, self).__init__()

  def get(self, id):
    if itemExists(id):
      return { 'item':marshal(getItem(id), item_fields) }
    abort(404)

  def put(self, id):
    if itemExists(id):
      args = self.reqparse.parse_args()
      deleteItem(id)
      item = Item(args['name'], args['description'], args['contact_info'], args['price'], args['user_id'], getCollegeIDFromUserID(args['user_id']), args['item_type'])
      addItem(item)
      return {'item' : marshal(item, item_fields)}, 201 
    abort(404)

  def delete(self, id):
    deleteItem(id)
    return {'result': True}

api.add_resource(ItemAPI, '/api/item/<int:id>', endpoint = 'item')

class ItemListAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    self.reqparse.add_argument('name', type = str, required = True, help = "No name provided", location = 'json')
    self.reqparse.add_argument('description', type = str, required = True, help = "No description provided", location = 'json')
    self.reqparse.add_argument('contact_info', type = str, required = True, help = "No contact_info provided", location = 'json')
    self.reqparse.add_argument('price', type = int, required = True, help = "No price provided", location = 'json')
    self.reqparse.add_argument('item_type', type = str, required = True, help = "No item_type provided", location = 'json')
    self.reqparse.add_argument('user_id', type = str, required = True, help = "No user_id provided", location = 'json')
    super(ItemListAPI, self).__init__()

  def get(self):
    return { 'items': map(lambda t: marshal(i, item_fields), getAllItems()) }

  def post(self):
    args = self.reqparse.parse_args()
    new_item = Item(args['name'], args['description'], args['contact_info'], args['price'], args['user_id'], getCollegeIDFromUserID(args['user_id']), args['item_type'])
    addItem(new_item)
    return {'item' : marshal(new_item, item_fields)}, 201

api.add_resource(ItemListAPI, '/api/items/', endpoint = 'items')

class ItemsByCollegeAPI(Resource):
  def _init__(self):
    super(ItemsByCollegeAPI, self).__init__()

  def get(self, id):
    return { 'items': map(lambda t: marshal(i, item_fields), getAllItemsByCollege()) }

api.add_resource(ItemsByCollegeAPI, '/api/college/<int:id>/items', endpoint = 'items_by_college')

class ItemsByUserAPI(Resource):
  def __init__(self):
    super(ItemsByUserAPI, self).__init__()

  def get(self, id):
    return { 'items': map(lambda t: marshal(i, item_fields), getAllItemsByUser()) }

api.add_resource(ItemsByUserAPI, '/api/user/<int:id>/items', endpoint = 'items_by_user')

class ItemsByTypeAPI(Resource):
  def __init__(self):
    super(ItemsByCollegeAPI, self).__init__()

  def get(self, type):
    return { 'items': map(lambda t: marshal(i, item_fields), getAllItemsByType()) }

api.add_resource(ItemsByTypeAPI, '/api/<string:type>/items', endpoint = 'items_by_type')

class ItemsByTextSearchAPI(Resource):
  def __init__(self):
    super(ItemsByTextSearchAPI, self).__init__()

  def get(self, text):
    return { 'items': map(lambda t: marshal(i, item_fields), getAllItemsByTextSearch()) }

api.add_resource(ItemsByTypeAPI, '/api/items/search/<string:text>', endpoint = 'items_by_search')



