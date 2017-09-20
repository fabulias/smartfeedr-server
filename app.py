from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from resources.information import Information
from common.database import *

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Information, '/')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    try:
        create_table()
    except:
        print ("Table schedule already exists")
    app.run(debug=True, host="127.0.0.1", port=8000)
