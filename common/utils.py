from datetime import datetime
class Utils:
    def convert_to_datetime(value):
        print ("type(value) => ",type(value))
        print ("value => ", value)
        value = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S')
        print ("value",type(value))
        return value

    def date_handler(x):
        if isinstance(x, datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    def and_params(a, b):
        print ("(a, b) => ", a, b)
        if (a == None and b == None):
            return True
        if (a != None and b == None):
            return False
        if (a == None and b != None):
            return False
        return True

    def second_parse_request(request_params):
        if(not(Utils.and_params(request_params['ration2'],request_params['date2']))):
            request_params['ration2']=0
            request_params['date2']=""
            return False
        if(not(Utils.and_params(request_params['ration3'],request_params['date3']))):
            request_params['ration3']=0
            request_params['date3']=""
            return False
        if(not(Utils.and_params(request_params['ration4'],request_params['date4']))):
            request_params['ration4']=0
            request_params['date4']=""
            return False
        return True
