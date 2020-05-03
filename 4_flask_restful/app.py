from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items: list = []

class Item(Resource):
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
            
        request_data = request.get_json()
        item = {
            "name": name,
            "price": request_data["price"]
        }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return { "items": items }

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)