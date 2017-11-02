from datetime import datetime
from crontab import CronTab

class Utils:
    def convert_to_datetime(value):
        print ("type(value) => ",type(value))
        print ("value => ", value)
        value = datetime.strptime(value,'%H:%M')
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
        if(not(Utils.and_params(request_params['ration1'],request_params['date1']))):
            request_params['ration1']=0
            request_params['date1']="00:00:00"
            return False
        if(not(Utils.and_params(request_params['ration2'],request_params['date2']))):
            request_params['ration2']=0
            request_params['date2']="00:00:00"
            return False
        if(not(Utils.and_params(request_params['ration3'],request_params['date3']))):
            request_params['ration3']=0
            request_params['date3']="00:00:00"
            return False
        if(not(Utils.and_params(request_params['ration4'],request_params['date4']))):
            request_params['ration4']=0
            request_params['date4']="00:00:00"
            return False
        return True

    def create_schedule(data):
        user_ = 'pi'
        my_cron = CronTab(user=user_)
        # Date1
        date_h = data['date1'].hour
        date_m = data['date1'].minute
        job = my_cron.new(command='python '+'/home/'+user_+'/Documents/smartfeedr-collector/motor.py '+ str(data['ration1']))
        job.hour.on(date_h)
        job.minute.on(date_m)
        my_cron.write()
        # Date2
        date_h = data['date2'].hour
        date_m = data['date2'].minute
        job = my_cron.new(command='python '+'/home/'+user_+'/Documents/smartfeedr-collector/motor.py '+ str(data['ration2']))
        job.hour.on(date_h)
        job.minute.on(date_m)
        my_cron.write()
        # Date3
        date_h = data['date3'].hour
        date_m = data['date3'].minute
        job = my_cron.new(command='python '+'/home/'+user_+'/Documents/smartfeedr-collector/motor.py '+ str(data['ration3']))
        job.hour.on(date_h)
        job.minute.on(date_m)
        my_cron.write()
        # Date4
        date_h = data['date4'].hour
        date_m = data['date4'].minute
        date_s = data['date4'].second
        job = my_cron.new(command='python '+'/home/'+user_+'/Documents/smartfeedr-collector/motor.py '+ str(data['ration4']))
        job.hour.on(date_h)
        job.minute.on(date_m)
        my_cron.write()
