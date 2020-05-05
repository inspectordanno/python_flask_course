from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items: list = []

class Item(Resource):
    # request parsing
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        # returns first item found by filter function; 
        # calling next again would return 2nd, 3rd, etc.
        # will not throw error if None is included; will return None
        item = next(filter(lambda item: item["name"] == name, items), None)
        #ternary if statement 
        return { "item": item }, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda item: item["name"] == name, items), None) is not None:
            return { "message": f"An item with name {name} already exists" }, 400
            
        request_data = Item.parser.parse_args()
        item = {
            "name": name,
            "price": request_data["price"]
        }
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        request_data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = { 'name': name, 'price': request_data['price'] }
            items.append(item)
        else:
            item.update(request_data) # update method for dictionaries
        return item


class ItemList(Resource):
    def get(self):
        return { "items": items }

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True) 