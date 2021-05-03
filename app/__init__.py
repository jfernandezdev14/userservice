from os import environ

from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = environ.get("MONGO_URI")
mongo_client = PyMongo(app)
db = mongo_client.db
CORS(app)
