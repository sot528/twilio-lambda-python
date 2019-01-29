from twilio.rest import Client
import urllib.parse
 
account_sid = 'AC.....'
auth_token = 'dd59a.....'

toPhoneNumber = ['+819012345678']

 
def call_handler(event, context):
    return call_exec(event)
 
def call_exec(params):
    client = Client(account_sid, auth_token)

    for to in toPhoneNumber:
        call = client.calls.create(
                                url='http://demo.twilio.com/docs/voice.xml',
                                to=to,
                                from_='+815012345678'
                            )
 
    return call.sid
