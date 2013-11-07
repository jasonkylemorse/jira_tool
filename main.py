import argparse
import subprocess
import datetime
import time
import requests
import call

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
    
print("Day", "\t", "Status", "\t", "Type", "\t", "Priority", "\t", "Total")  # Print a tab seperated list of results
loop_day = start_day  # Initialise the Loop
while loop_day > start_day - days:
    day = datetime.date.fromordinal(datetime.date.today().toordinal() + loop_day)  # Get the Day the request is for
    eod = str(loop_day)
    for status in statuses:  # Loop through Statuses provided
        for type in types:  # Loop through the Types provided
            for priority in priorities:
                total = call.search(target, api_path, project, type, priority, status, eod)
                
                print(day, "\t", status, "\t", type, "\t", priority, "\t", total)  # Print a tab seperated list of results
    loop_day -= 1  # Increment the loop, we are going back in time so -1
