#!/usr/bin/python3

import subprocess, sys, json

server_ip = "69.55.55.84"
port = "8080"

def create_session():
    new_session_process = subprocess.Popen("otree create_session public_goods 1".split(), stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd="../")

    new_session_process.wait()

    # open stderr for the session id
    output = new_session_process.communicate()[1]

    new_session_id = str(output).split()[-1][:8]

    return new_session_id

def get_url(session_id):
    get_session_info_process = subprocess.Popen(["wget", "http://" + server_ip + ":8080/SessionStartLinks/" + session_id], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    get_session_info_process.wait()

    with open(session_id, "r") as output:

        subprocess.Popen(["rm", session_id])

        output = output.read()

        index_of_link = output.find("/join/")

        return output[index_of_link + 6: index_of_link + 16]


sessions = []

try: 
    num_sessions = int(sys.argv[1])
except:
    num_sessions = 1

for i in range(0, num_sessions):
    session_id = create_session()
    session_url = get_url(session_id)
    sessions.append(session_url)
    print(i, " id: ", session_id)

with open("sessions.json", "w") as session_list:
    session_list.write(json.dumps(sessions))
