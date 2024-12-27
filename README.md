Using cURL for Testing
1. Create: c
2. Retrieve:
- Retrieve all: curl -X GET http://127.0.0.1:5000/products
- Retrieve one: curl -X GET http://127.0.0.1:5000/products/1
3. Update: curl -X PUT http://127.0.0.1:5000/products/1 -H "Content-Type: application/json" -d '{"name": "Laptop", "price": 1300, "quantity": 6}'
4. Delete: curl -X DELETE http://127.0.0.1:5000/products/1