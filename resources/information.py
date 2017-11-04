from flask_restful import Resource, reqparse
from flask import request
import datetime
import json
from common.utils import Utils
import os

class Information(Resource):
    def post(self):
        input_data = request.get_json(force=True)
        print (input_data)
        if not Utils.first_parser(input_data):
            response = {
                'message':'Error sending params, the parameters are in pairs'
            }
            return response, 400

        if (not(Utils.second_parse_request(input_data))):
            response = {
                'message':'Error sending params, the parameters are in pairs'
            }
            return response, 406
        
        os.system("crontab -r")
        try:
            Utils.create_schedule(input_data)
        except:
             response = {
                'data':"Internal server error with crontab"
             }
             return response, 500
        response = {
            'data':'Schedule created with success'
        }
        return response, 200
