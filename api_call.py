import argparse
import subprocess
import datetime
import time
import requests

# Config vars
target = "http://pvjira01.pv.local:8080"
# logfile = "api_call.log"
statuses = ["Open", "ReOpened", "Scheduled", "In Progress", "Code Review", "Functional Review", "Resolved", "Closed"]
# statuses = ["Scheduled",'In Progress","Code Review','Functional Review","Resolved","Closed']
types = ["Bug", "Task", "Epic", "Story"]
priorities = ["Blocker", "Critical", "Major", "Minor", "Trivial"]
days = 180
start_day = -1
api_path = '/rest/api/2/search?jql='
project = "spui"

# Arguments handler
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Target Host")
# parser.add_argument("-l", "--logfile", help="Logfile")
args = parser.parse_args()

if args.target:    
    target = str(args.target)
loop_day = start_day  # Initialise the Loop
while loop_day > start_day - days:
    day = datetime.date.fromordinal(datetime.date.today().toordinal() + loop_day)  # Get the Day the request is for
    for status in statuses:  # Loop through Statuses provided
        for type in types:  # Loop through the Types provided
            for priority in priorities:
                jql = ' ' .join(['project=' + project + '+AND+issueType="' + type + '"+and+priority+was+in("' + priority + '")+ON+endofDay(' + str(loop_day) + ')+and+status+was+in+("' + status + '")+ON+endofDay(' + str(loop_day) + ')'])  # Combine the vars for the JQL query
                run = ' ' .join([target + api_path + jql])  # combine the vars to get the full query
#                 print(run)
                r = requests.get(run)  # Use requests library to make a http request to the string defined in 'run'
                total = r.json().get('total')  # Response is JSON and we are aftet the 'total' value
                print(day, "\t", status, "\t", type, "\t", priority, "\t", total)  # Print a tab seperated list of results
    loop_day -= 1  # Increment the loop, we are going back in time so -1
