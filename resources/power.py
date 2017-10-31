from flask_restful import Resource, reqparse
from flask_restful import inputs
import os
import subprocess, signal

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
            status = subprocess.Popen("python ../smartfeedr-collector/test.py", shell=True)
            response = {
                'data':''
            }
            return response, 200
        else:
            p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            for line in out.splitlines():
                file_=b'test.py'
                if file_ in line:
                    line = line.decode("utf-8")
                    print ("[Process to kill]", line)
                    pid = int(line.split(None, 1)[0])
                    os.kill(pid, signal.SIGKILL)
                    response = {
                        'data':line
                    }
                    return response, 200
            response = {
                'data':''
            }
            return response, 404


    def get(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            file_=b'test.py'
            if file_ in line:
                line = line.decode("utf-8")
                print ("[Assigned process]", line)
                pid = int(line.split(None, 1)[0])
                response = {
                    'data':line
                }
                return response, 200
        response = {
            'data':''
        }
        return response, 404
