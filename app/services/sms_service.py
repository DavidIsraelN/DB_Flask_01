import re
from app.repositories.twilio_repository import TwilioRepository


class SmsService:
    PHONE_REGEX = re.compile(r'^\+9725\d{8}$')  # israeli number


    def __init__(self):
        self.repo = TwilioRepository()


    def send_sms(self, data):
        to = data.get('to')
        message = data.get('message')

        print(f"to is {to}, message is {message}")

        if not to or not message:
            raise ValueError("Both 'to' and 'message' are required")
        if not self.PHONE_REGEX.match(to):
            raise ValueError(
                "Invalid Israeli mobile number format, "
                "must be +9725 followed by 8 digits, e.g. +972501234567"
            )

        return self.repo.send_message(to, message)
