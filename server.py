import flask as fl
import sqlite3
import sys
import os
from flask import request
import json
from datetime import datetime
from crontab import CronTab

app = fl.Flask(__name__)

def and_params(a, b):
        if (a == None and b == None):
            return True
        if (a != None and b == None):
            return False
        if (a == None and b != None):
            return False
        return True

def parse_request(request_params):
        if(not(and_params(request_params['ration1'],request_params['date1']))):
            request_params['ration1']=0
            request_params['date1']="00:00:00"
            return False
        if(not(and_params(request_params['ration2'],request_params['date2']))):
            request_params['ration2']=0
            request_params['date2']="00:00:00"
            return False
        if(not(and_params(request_params['ration3'],request_params['date3']))):
            request_params['ration3']=0
            request_params['date3']="00:00:00"
            return False
        if(not(and_params(request_params['ration4'],request_params['date4']))):
            request_params['ration4']=0
            request_params['date4']="00:00:00"
            return False
        return True

def create_schedule(data):
  my_cron = CronTab(user='fabulias')
  # Date1
  date_h = data['date1'].hour
  date_m = data['date1'].minute
  job = my_cron.new(command='python '+os.getcwd()+'/main.py '+ str(data['ration1']))
  job.hour.on(date_h)
  job.minute.on(date_m)
  my_cron.write()
  # Date2
  date_h = data['date2'].hour
  date_m = data['date2'].minute
  job = my_cron.new(command='python '+os.getcwd()+'/main.py '+ str(data['ration2']))
  job.hour.on(date_h)
  job.minute.on(date_m)
  my_cron.write()
  # Date3
  date_h = data['date3'].hour
  date_m = data['date3'].minute
  job = my_cron.new(command='python '+os.getcwd()+'/main.py '+ str(data['ration3']))
  job.hour.on(date_h)
  job.minute.on(date_m)
  my_cron.write()
  # Date4
  date_h = data['date4'].hour
  date_m = data['date4'].minute
  date_s = data['date4'].second
  job = my_cron.new(command='python '+os.getcwd()+'/main.py '+ str(data['ration4']))
  job.hour.on(date_h)
  job.minute.on(date_m)
  my_cron.write()

@app.route("/")
def index():
  return json.dumps({"message":"Incorrect route, please try with method POST"}),

@app.route("/", methods=['POST'])
def schedule():
  os.system("crontab -r")
  data = request.get_json()

  try:
    parse_request(data)
  except:
    response = {
          'message':'Error sending params, the parameters are in pairs'
    }
    return json.dumps(response), 406

  # Convert strings to datetime type
  try:
    data['date1'] = datetime.strptime(data['date1'], '%H:%M:%S')
    data['date2'] = datetime.strptime(data['date2'], '%H:%M:%S')
    data['date3'] = datetime.strptime(data['date3'], '%H:%M:%S')
    data['date4'] = datetime.strptime(data['date4'], '%H:%M:%S')
  except:
    response = {
        'message':"Format error in dates"
    }
    return json.dumps(response), 400
  try:
    create_schedule(data)
  except:
    response = {
        'message':"Internal server error with crontab"
    }
    return json.dumps(response), 500

  response = {
      'message':"Schedule created with success"
  }

  return json.dumps(response), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
