import argparse
import subprocess
import platform
import time

# Config vars
target = "http://pvjira01.pv.local:8001"
logfile = "api_call.log"
username = "jsaxon"
password = "aaaaaa"
statuses =["Scheduled","In Progress","Code Review","Functional Review","Resolved","Closed"]
days = 1
start_day = -1

command =' '.join(['curl -D- -u',username+':'+password,'-X GET -H "Content-Type: application/json"'])
api_path = '/rest/api/2/search?jql='


platform = platform.system()
if platform == "Linux":
   command = "curl"
# elif platform == "Windows":
#    command = "..."
else:
   print("Unsupported System")
   exit

# Arguments handler
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Target Host")
parser.add_argument("-l", "--logfile", help="Logfile")
args = parser.parse_args()

if args.target:    
    target = str(args.target)
if args.logfile:
    logfile = str(args.logfile)
     
# jql='project=spui+AND+status+was+"Closed"+ON+endofDay(-1)'
# run = ' ' .join([command,",target+api_path+jql,"])
# print(run)
# print("aaaa")

loop_day = start_day
while loop_day > start_day - days:
#     print(loop_day)
    for status in statuses:
#         print(status)
         jql=' ' .join(['project=spui+AND+status+was+"'+status+'"+ON+endofDay('+str(loop_day)+')"'])
         run = ' ' .join([command,'"'+target+api_path+jql])
         print(run)
    loop_day -= 1
