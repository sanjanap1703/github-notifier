import os
from twilio.rest import Client

account_sid = os.environ['sid']
auth_token = os.environ['token']
to_whatsapp_no = os.environ['whatsapp_no']
from_whatsapp_no = os.environ['from_whatsapp_no']

client = Client(sid,token)

message = client.messages.create(
                              body='Code Pushed in main branch of https://github.com/sanjanap1703/github-notifier',
                              from_='whatsapp:'+from_whatsapp_no,
                              to='whatsapp:'+whatsapp_no
                          )

print("Message ID:",message.sid)
