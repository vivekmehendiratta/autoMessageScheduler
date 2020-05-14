# imports
from message_data import *
import requests
from datetime import datetime
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler


class AutoMessage():

    def __init__(self, message, language, numbers):
        self.url = "https://www.fast2sms.com/dev/bulk"
        self.message = message
        self.language = language
        self.numbers = numbers

    def getPayload(self):
        payload = createPayload(message=self.message, language=self.language, numbers=self.numbers)

        return payload

    def getHeaders(self):
        headers = createHeaders()

        return headers

    def sendResponse(self):
        payload = self.getPayload()
        headers = self.getHeaders()
        method = 'POST'
        response = requests.request(method, self.url, data=payload, headers=headers)
        return response


def job():
    auto_message = AutoMessage(message='Please Stand Up and Drink Water',
                               language='english', numbers='9876543210')
    auto_response = auto_message.sendResponse()
    print(auto_response.text)


while 1:
    hour_list = list(range(10, 23))
    now = datetime.now()
    if((now.hour in hour_list) & (now.minute == 0)):
        job()
        sleep(70)
