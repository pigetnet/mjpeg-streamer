#!/usr/bin/python
import json
import os.path
import sys
default_conf = '/opt/piget/mjpeg-streamer/default/'
user_conf = '/opt/user/config/camera/'
password_conf = '/opt/user/config/camera/password.json'
default_conf = default_conf + str(sys.argv[1])
user_conf = user_conf + str(sys.argv[1])
#print sys.argv[1]
pre_args = ""
args = ""
if(os.path.exists(user_conf)):
    choose_conf = user_conf
elif(os.path.exists(default_conf)):
    choose_conf = default_conf
else:
    choose_conf = False

if(os.path.exists(password_conf)):
    password_conf = password_conf
else:
    password_conf = False

# print choose_conf
if choose_conf is not False:
    try:
        with open(choose_conf) as config_file:
            config = json.load(config_file)
            for k, v in config.items():
                #if(k == "c"):
                #    pre_args = pre_args + "--" + str(k) + " " + str(v) + " "
                #else:
                args = args + "--" + str(k) + " " + str(v) + " "
    except ValueError as e:
        print e
        exit(1)

if password_conf is not False:
    try:
        with open(password_conf) as password_file:
            password = json.load(password_file)
            for k, v in password.items():
                if(k == "c"):
                    pre_args = pre_args + "--" + str(k) + " " + str(v) + " "
    except ValueError as e:
        print e
        exit(1)

print pre_args
print args
