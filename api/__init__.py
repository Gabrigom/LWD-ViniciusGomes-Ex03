from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api_mitologia'

api = Api(app)
mongo = PyMongo(app)
mm = Marshmallow(app)

from .resources import mito_resource