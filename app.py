from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for
from resources.information import Information
from resources.power import Power

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Information, '/information')
api.add_resource(Power, '/')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5023)
