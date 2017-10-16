from flask_restful import Resource, reqparse
import datetime
import json
from common.utils import Utils

class Information(Resource):
    def post(self):
        data=None
        parser = reqparse.RequestParser()
        parser.add_argument('ration1', type=float, location='json', required=True, help='Ration1 cannot be converted')
        parser.add_argument('date1', type=Utils.convert_to_datetime, location='json', required=True, help='Date1 cannot be converted')
        parser.add_argument('ration2', type=float,location='json', help='Ration2 cannot be converted')
        parser.add_argument('date2', type=Utils.convert_to_datetime,location='json', help='Date2 cannot be converted')
        parser.add_argument('ration3', type=float,location='json', help='Ration3 cannot be converted')
        parser.add_argument('date3', type=Utils.convert_to_datetime,location='json', help='Date3 cannot be converted')
        parser.add_argument('ration4', type=float,location='json', help='Ration4 cannot be converted')
        parser.add_argument('date4', type=Utils.convert_to_datetime,location='json', help='Date4 cannot be converted')
        request_params = parser.parse_args()
        #print ("[request_params]",request_params)
        if (not(Utils.second_parse_request(request_params))):
            response = {
                'message':'Error sending params, the parameters are in pairs'
            }
            return response, 406
        #Insert request data in database
        insert_data(request_params)
        response = {
            'data':json.dumps(request_params, default=Utils.date_handler)
        }
        return response, 200
