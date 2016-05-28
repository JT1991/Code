from twilio.rest import TwilioRestClient

account_sid = "{{AC06f77179cc9750a4b4238642a9583e7d}}" # Your Account SID from www.twilio.com/console
auth_token  = "{{64e2c059c80e783fc1922f315711ac00}}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from me.",
    to="+07804242120",    # Replace with your phone number
    from_="+441908410629") # Replace with your Twilio number
print(message.sid)
