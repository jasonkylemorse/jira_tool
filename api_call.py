import argparse
import subprocess
import datetime
import time
import requests

# Config vars
target = "http://pvjira01.pv.local:8080"
logfile = "api_call.log"
# statuses = ["Scheduled","In Progress","Code Review","Functional Review","Resolved","Closed"]
statuses = ["Scheduled",'In Progress","Code Review','Functional Review","Resolved","Closed']
types = ["Bug","Task","Epic","Story"]
days = 180
start_day = -1

# command =' '.join(['curl -D- -u',username+':'+password,'-X GET -H "Content-Type: application/json"'])
api_path = '/rest/api/2/search?jql='

# Arguments handler
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Target Host")
parser.add_argument("-l", "--logfile", help="Logfile")
args = parser.parse_args()

if args.target:    
    target = str(args.target)
if args.logfile:
    logfile = str(args.logfile)
 
log = open("logfile", "w")
    
loop_day = start_day
while loop_day > start_day - days:
#     print(loop_day)
    day = datetime.date.fromordinal(datetime.date.today().toordinal()+loop_day)
#     print(day)
    for status in statuses:
#         print(status)
        for type in types:
#             print(type)
            jql=' ' .join(['project=spui+AND+issueType="'+type+'"+and+status+was+in+("'+status+'")+ON+endofDay('+str(loop_day)+')'])
            run = ' ' .join([target+api_path+jql])
#             print(run)
            r = requests.get(run)
            total = r.json().get('total')
            print(day,"\t",status,"\t",type,"\t",total)
    loop_day -= 1