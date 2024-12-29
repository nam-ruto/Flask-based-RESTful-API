from flask import Flask, jsonify, request
from threading import Lock

app = Flask(__name__)

# General configuration
SUCCESS_CODE = 200
CREATED_CODE = 201
BAD_REQUEST_CODE = 400
NOT_FOUND_CODE = 404
SERVER_ERROR_CODE = 500
MISSING_FIELD = "Missing required fields: 'name', 'price', 'quantity'"
PRODUCT_NOT_FOUND = "Product not found:"
FAIL_REQUEST = "Request body must be JSON"


# --- In-memory data structure ---
products = {} # Store the product fields: id, name, price, quantity
products_id_counter = 1
lock = Lock()


# --- ERROR Response ---
def error_response(message, status_code):
    return jsonify({
        "error": message
    }), status_code


# --- Home: root URL ---
@app.route('/')
def home():
    return jsonify({"message": "Backend API assessment!"}), SUCCESS_CODE


# --- CREATE a new product (POST request) ---
@app.route('/products', methods=['POST'])
def add_product():
    global products_id_counter
    data = request.get_json()
    if (not data) or ('name' not in data) or ('price' not in data) or ('quantity' not in data):
        return error_response(message=MISSING_FIELD, status_code=BAD_REQUEST_CODE) #400
    
    with lock:
        product_id = products_id_counter
        products[product_id] = {
            'id': product_id,
            'name': data['name'],
            'price': data['price'],
            'quantity': data['quantity']
        }
        products_id_counter += 1
    
    return jsonify(products[product_id]), CREATED_CODE #201


# --- RETRIEVE all products (GET request) ---
@app.route('/products', methods=['GET'])
def get_all():
    return jsonify(list(products.values())), SUCCESS_CODE #200


# --- RETRIEVE a specific product (GET request) ---
@app.route('/products/<int:product_id>', methods=['GET'])
def get_one(product_id:int):
    product = products.get(product_id)
    if not product:
        return error_response(message=f"Product not found: {product_id}", status_code=NOT_FOUND_CODE)
    return jsonify(product), SUCCESS_CODE #200


# --- UPDATE a product by id (PUT request)
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id:int):
    data = request.get_json()
    if not data:
        return error_response(FAIL_REQUEST, 400)
    
    product = products.get(product_id)
    if not product:
        return error_response(message=f"Product not found: {product_id}", status_code=NOT_FOUND_CODE) #404
    
    with lock:
        product.update({
            'name': data.get('name', product['name']),
            'price': data.get('price', product['price']),
            'quantity': data.get('quantity', product['quantity'])
        })
    
    return jsonify(product), 200


# --- DELETE a product by id (DELETE request)
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id:int):
    with lock:
        product = products.pop(product_id, None)
        if not product:
            return error_response(message=f"Product not found: {product_id}", status_code=NOT_FOUND_CODE) #404
        
    return jsonify({
        'message': f"Product with ID {product_id} is deleted successfully",
        'deleted product': product
    }), 200


# --- ERROR HANDLER: Invalid JSON input ---
@app.errorhandler(400)
def handle_bad_request(e):
    return error_response(message="Invalid JSON or request format", status_code=BAD_REQUEST_CODE) #400


# --- ERROR HANDLER: General servel error ---
@app.errorhandler(500)
def handle_server_error(e):
    return error_response(message="Internal server error", status_code=SERVER_ERROR_CODE) #500


# --- Main funtion ---
if __name__ == '__main__':
    app.run(debug=True)
