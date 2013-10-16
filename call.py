import requests

def search(target, api_path, project, type, priority, status, eod):
    jql = ' ' .join(['project=' + project + '+AND+issueType="' + type + '"+and+priority+was+in("' + priority + '")+ON+endofDay(' + eod + ')+and+status+was+in+("' + status + '")+ON+endofDay(' + eod + ')'])  # Combine the vars for the JQL query
    run = ' ' .join([target + api_path + jql])  # combine the vars to get the full query
    #                 print(run)
    r = requests.get(run)  # Use requests library to make a http request to the string defined in 'run'
    total = r.json().get('total')  # Response is JSON and we are aftet the 'total' value
    return(total)
