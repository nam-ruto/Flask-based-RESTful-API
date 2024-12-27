## Flask-based RESTful API: Product Management

### I. Description

This is a Flask-based RESTful API designed for managing a collection of products. The API supports **CRUD** operations such as adding, retrieving, updating, and deleting products. It uses an in-memory data structure for testing purposes and is thread-safe to handle concurrent requests.

### II. Features

- Create/Add a new product (`POST /products`)
- Retrieve all products (`GET /products`)
- Retrieve a specific product by ID (`GET /products/<id>`)
- Update a product by ID (`PUT /products/<id>`)
- Delete a product by ID (`DELETE /products/<id>`)

### III. Requirements

- Python 3.7 or higher
- Flask library: run this command `pip install flask` or you can install all needed dependencies using `pip install -r requirements.txt`

### IV. Usage

1. Start the Flask Application:
- Run the following command: `python app.py`
- The server will start and be accesible at the root endpoint: `http://127.0.0.1:5000`
2. Verify the Server is Running:
- Open your web browser or use a tool like `curl` or `Postman` to navigate to the root endpoint.
- If you see a welcome message like the following:
  ```json
  {
    "message": "Backend API assessment!"
  }
  ```
  The server is running successfully, and you can proceed to test API requests.

### V. Testing

There are several options to test the API, such as `curl`, `Postman`, or `SoapUI`. For simplicity, this guide uses `curl` commands. Ensure the server is running before proceeding (`http://127.0.0.1:5000`). You can test the API using these cURL commands:
1. Create:
```
curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "Laptop", "price": 1200, "quantity": 10}'
```
2. Retrieve:
- Retrieve all: `curl -X GET http://127.0.0.1:5000/products`
- Retrieve one: `curl -X GET http://127.0.0.1:5000/products/1`
3. Update:
```
curl -X PUT http://127.0.0.1:5000/products/1 -H "Content-Type: application/json" -d '{"name": "Laptop", "price": 1300, "quantity": 6}'
```
4. Delete:
```
curl -X DELETE http://127.0.0.1:5000/products/1
```
