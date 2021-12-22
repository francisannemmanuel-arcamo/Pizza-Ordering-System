# Create a string parser for SMS messages and create a class to handle them

import re


class SMS:
    def __init__(self, string):
        self.string = string
        self.sms_dict = {}
        self.parse_string()

    def parse_string(self):
        # Get the date and time
        date_time = re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}', self.string)
        self.sms_dict['date_time'] = date_time.group(0)

        # Get the name of the person who sent the message
        name = re.search(r'\w+', self.string)
        self.sms_dict['name'] = name.group(0)

        # Get the message
        message = re.search(r'\w+', self.string)
        self.sms_dict['message'] = message.group(0)

    def get_date_time(self):
        return self.sms_dict['date_time']

    def get_name(self):
        return self.sms_dict['name']

    def get_message(self):
        return self.sms_dict['message']