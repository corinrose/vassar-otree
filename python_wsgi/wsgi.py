from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import json, os, subprocess

def trigger():

    current_session = 0

    with open("sessions.json", "r") as fp:
        sessions = json.loads(fp.read())
        sessions = sessions[1:]
        
        with open("sessions.tmp", "w") as tmp:
            tmp.write(json.dumps(sessions))

    os.remove("sessions.json")
    subprocess.Popen(["mv", "sessions.tmp", "sessions.json"]).wait()

    with open("sessions.json", "r") as fp:
        sessions = json.loads(fp.read())
        return sessions[0]

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    session = trigger()
    
    status = '200 OK'
    headers = [('Access-Control-Allow-Origin', '*'), ('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]

    ret.append((str.encode("session: %s" % session)))

    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
