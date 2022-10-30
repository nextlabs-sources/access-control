#!/bin/bash

zip -r9 send-trial-credentials.zip . -x "deploy.sh"

aws lambda update-function-code --region "us-west-2" --function-name "send-trial-credentials" --zip-file fileb://send-trial-credentials.zip --profile devops

rm send-trial-credentials.zip
