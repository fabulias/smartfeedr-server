from flask_restful import Resource, reqparse
from flask_restful import inputs
import os
import subprocess, signal
import json
import flask

class Power(Resource):
    """docstring for Power."""
    def post(self):
        data=None
        parser = reqparse.RequestParser()
        parser.add_argument('state', type=inputs.boolean, help="Bad input state!!!")
        request_params = parser.parse_args()
        if request_params['state']==None:
            response = {
                'data':''
            }
            return response, 406
        if request_params['state']:
            status = subprocess.Popen("python ../smartfeedr-collector/ultrasonic.py", shell=True)
            response = {
                'data':''
            }
            return response, 200
        else:
            p = subprocess.Popen(['ps', '-f'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            for line in out.splitlines():
                file_=b'ultrasonic.py'
                if file_ in line:
                    line = line.decode("utf-8")
                    print ("[Process to kill]", line)
                    pid = int(line.split(None, 1)[1].split()[0])
                    subprocess.Popen("pkill -f ultrasonic.py", shell=True)
                    response = {
                        'data':line
                    }
                    return response, 200
            response = {
                'data':''
            }
            return response, 204


    def get(self):
        p = subprocess.Popen(['ps', '-f'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            file_=b'ultrasonic.py'
            if file_ in line:
                line = line.decode("utf-8")
                print ("[Assigned process]", line)
                pid = int(line.split(None, 1)[1].split()[0])
                response = {
                    'data':line
                }
                return response, 200
        response = {
            'data':'i'
        }
        print ("HARAAA")
        return flask.jsonify(response), 204
