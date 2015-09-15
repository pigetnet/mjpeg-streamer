#!/usr/bin/python
import json
import os.path
import sys
password_conf = '/opt/user/config/camera/password.json'

if(os.path.exists(password_conf)):
    password_conf = password_conf
else:
    password_conf = False

pre_args = ""

if password_conf is not False:
    try:
        with open(password_conf) as password_file:
            password = json.load(password_file)
            for k, v in password.items():
                if(k == "c"):
                    pre_args = "-u" + str(v)
    except ValueError as e:
        #print e
        exit(1)

print pre_args
