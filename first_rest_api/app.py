from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99    
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() 
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    match = [store for store in stores if store['name'] == name]
    if not match: 
       return jsonify({ 'message': 'store not found' })
    else:
        return jsonify(match[0])

#GET /store
@app.route('/store/', methods=['GET'])
def get_stores():
    return jsonify({ 'stores': stores })

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if store['name'] == name:
            stores['items'].append(item)
            return jsonify(new_item)
    return jsonify({ 'message': 'store not found' })

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({ 'items': store['items'] })
    return jsonify({ 'message': 'store not found' })

app.run(port=5000)