from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC.....'
auth_token = 'dd59ae.....'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+819012345678',
                        from_='+819012345679'
                    )

print(call.sid)
