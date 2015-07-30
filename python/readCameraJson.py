#!/usr/bin/python
import json
import os.path
import sys
default_conf = '/opt/piget/camera/default/'
user_conf = '/opt/user/config/camera/'
default_conf = default_conf + str(sys.argv[1])
user_conf = user_conf + str(sys.argv[1])
print sys.argv[1]
pre_args = ""
args = ""
if(os.path.exists(user_conf)):
    choose_conf = user_conf
elif(os.path.exists(default_conf)):
    choose_conf = default_conf
else:
    choose_conf = False

# print choose_conf
if choose_conf is not False:
    try:
        with open(choose_conf) as config_file:
            config = json.load(config_file)
            for k, v in config.items():
                if(k == "c"):
                    pre_args = pre_args + "--" + str(k) + " " + str(v) + " "
                else:
                    args = args + "--" + str(k) + " " + str(v) + " "
    except ValueError as e:
        print e
        exit(1)

print pre_args
print args
