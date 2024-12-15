from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

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



app.run(debug=True)