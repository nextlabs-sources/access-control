import json
import requests
from requests.auth import HTTPDigestAuth

def lambda_handler(event, context):
    # TODO implement
    # Replace with the correct URL

    # [BITBUCKET-BASE-URL], i.e.: https://bitbucket.org/
    url = '[BITBUCKET-BASE-URL]/api/1.0/user/'
    headers = {'Content-Type': 'application/json'}

    # get user
    # [USERNAME], i.e.: myuser
    # [PASSWORD], i.e.: itspassword
    r = requests.get(url, auth=('[USERNAME]', '[PASSWORD]'), headers=headers)
    print(r.status_code)
    print(r.text)
    #print(r.content)

    url = "http://api_url"
    myResponse = requests.get(url,auth=HTTPDigestAuth(raw_input("username: "), raw_input("Password: ")), verify=True)
    #print (myResponse.status_code)

    if(myResponse.ok):
        # Loading the response data into a dict variable
        # json.loads takes in only binary or string variables so using content to fetch binary content
        # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
        jData = json.loads(myResponse.content)

        print("The response contains {0} properties".format(len(jData)))
        print("\n")
        for key in jData:
            print key + " : " + jData[key]
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler("-","---")

