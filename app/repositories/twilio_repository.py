from twilio.rest import Client
import os

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_number = os.getenv('TWILIO_PHONE_NUMBER')
my_number = os.getenv('MY_PHONE_NUMBER')


class TwilioRepository:
    def __init__(self):
        self.client = Client(account_sid, auth_token)


    def send_message(self, to_phone, message):
        print(f"im sending message to {to_phone}, from {from_number}, and message is: {message}")
        return self.client.messages.create(to=my_number,
                                           from_=from_number,
                                           body=message)
