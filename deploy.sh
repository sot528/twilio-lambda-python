rm -f call.zip
zip -r call.zip .
aws --region us-west-2 lambda update-function-code --function-name twilio-python --zip-file fileb://call.zip
