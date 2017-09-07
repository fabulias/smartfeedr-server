from flask_restful import Resource, reqparse
import datetime
import json
from common.utils import Utils

def convert_to_datetime(value):
    print ("type(value) => ",type(value))
    print ("value => ", value)
    value = datetime.datetime.strptime(value,'%Y-%m-%dT%H:%M:%S')
    print ("value",type(value))
    return value

def date_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")
#value =>  2017-03-01T10:10:10

#lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S')

def second_parse_request(request_params):
    for value in request_params:
        print ("value => ", request_params[value])

class Information(Resource):
    def post(self):
        data=None
        parser = reqparse.RequestParser()
        parser.add_argument('ration1', type=float, location='json', required=True, help='Ration1 cannot be converted')
        parser.add_argument('date1', type=convert_to_datetime, location='json', required=True, help='Date1 cannot be converted')
        parser.add_argument('ration2', type=float,location='json', help='Ration2 cannot be converted')
        parser.add_argument('date2', type=convert_to_datetime,location='json', help='Date2 cannot be converted')
        parser.add_argument('ration3', type=float,location='json', help='Ration3 cannot be converted')
        parser.add_argument('date3', type=convert_to_datetime,location='json', help='Date3 cannot be converted')
        parser.add_argument('ration4', type=float,location='json', help='Ration4 cannot be converted')
        parser.add_argument('date4', type=convert_to_datetime,location='json', help='Date4 cannot be converted')
        request_params = parser.parse_args()
        print ("here ->  ", request_params['ration1'])
        second_parse_request(request_params)
        print ("[request_params]",request_params)
        response = {
            'data':json.dumps(request_params, default=date_handler),
            'status':200
        }
        return response
