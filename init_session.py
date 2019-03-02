#!/usr/bin/python3

import subprocess

# new session cmd: "otree create_session dictator_goods 1"

out = ""
#new_session_process = subprocess.call("/usr/bin/otree create_session dictator_goods 1")
new_session_process = subprocess.Popen("otree create_session dictator_goods 1".split(), stdout=subprocess.PIPE)

new_session_process.wait()

output, error = new_session_process.communicate()

print(output)
