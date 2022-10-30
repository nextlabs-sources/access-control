import json
import requests
from requests.auth import HTTPDigestAuth

def lambda_handler(event, context):
    # TODO implement
    # Replace with the correct URL

    # [BITBUCKET-BASE-URL], i.e.: https://bitbucket.org/
    url = 'https://bitbucket.org/pi/2.0/user/'
    headers = {'Content-Type': 'application/json'}

    # get user
    # [USERNAME], i.e.: myuser
    # [PASSWORD], i.e.: itspassword
    r = requests.get(url, auth=('gKL7ETETqwdgmhPF6A', 'KH56Y5b9sB9yPMQYnFh42PSsAyUtfTFk'), headers=headers)
    print(r.status_code)
    print(r.text)
    #print(r.content)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

lambda_handler("-","-")