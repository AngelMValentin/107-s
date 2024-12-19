import pymongo
import certifi

# this is the connection string that I got from the mongoDB connection
con_string = "mongodb+srv://angel:!Q!Q!Q!Q1q1q1q1q@cluster0.z8wzb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(con_string, tlsCAFile = certifi.where())
db = client.get_database("Tacos")

