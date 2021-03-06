import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = """
        --sql
        SELECT * FROM items WHERE name=?
        ;
        """
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {"item": { "name": row[0], "price": row[1] } }
        return { "message": "Item not found" }, 404
    
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