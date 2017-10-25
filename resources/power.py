from flask_restful import Resource, reqparse
from flask_restful import inputs
import os
import subprocess

class Power(Resource):
    """docstring for Power."""
    def post(self):
        data=None
        parser = reqparse.RequestParser()
        parser.add_argument('state', type=inputs.boolean, help="Bad input state!!!")
        request_params = parser.parse_args()
        print (request_params['state'])
        print ("type ", type(request_params['state']))
        if request_params['state']:
            status = subprocess.call("bash ../smartfeedr-collector/asd.sh", shell=True)
        else:
            print ("chaoooo")
