import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.authToken)

TwilioNumber = '+14027288634'

mycellphone = '+12815095363'

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber,
                                     body="Hey there!")

print(textmessage.status)

call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                           to=myCellPhone,from_=TwilioNumber)