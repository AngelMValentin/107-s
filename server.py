from flask import Flask, request
import json
from config import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/hello")
def hello():
    message = {'message': 'Hello there!'}
    return  json.dumps(message)

@app.get("/test")
def test():
    return "Hello from the test page"

@app.get("/about")
def about():
    return "Angel Valentin"

@app.get("/contact")

def contact():
    contactPage = "This is the contact page"
    return json.dumps(contactPage)

@app.get("/api/products")
def get_products():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

@app.post("/api/products")
def save_product():
    product = request.get_json()
    print(f"this is my new product {product}")
    # products.append(product)
    db.products.insert_one(product)
    product = fix_id(product)
    return json.dumps(product)


@app.get('/api/categories')
def get_categories():
    results = []
    cursor = db.products.find({})
    for prod in cursor:
        category = prod['category']
        if category not in results:
            results.append(category)

    return json.dumps(results)


@app.get("/api/coupons")
def get_coupons():
    coupons = []
    cursor = db.coupons.find({})
    for coupon in cursor:
        coupons.append(fix_id(coupon))
    return json.dumps(coupons)

@app.post("/api/coupons")
def save_coupon():
    coupon = request.get_json()
    print(f"this is my new coupon {coupon}")
    # products.append(product)
    db.coupons.insert_one(coupon)
    coupon = fix_id(coupon)
    return json.dumps(coupon)

@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")

    if 0 <= index <= len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"
    
products = []
    
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >=0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else: 
        "That index does not exist"

    

app.run(debug=True)