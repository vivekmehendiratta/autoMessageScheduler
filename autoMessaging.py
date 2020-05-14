# imports
from message_data import *
import requests
from datetime import datetime
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
    auto_response = anki_message.sendResponse()
    print(auto_response.text)

    time = datetime.now()
    if(time.hour >= 22):
        scheduler.remove_job('water_reminder')


global scheduler
scheduler = BlockingScheduler()
print('scheduler instantiated')

scheduler.add_job(job, 'interval', hours=1, id='water_reminder')
print('job added')

start_job = False
while 1:
    now = datetime.now()
    if(now.hour == 15):
        start_job = True
        break

if(start_job):
    print('Starting the scheduler')
    scheduler.start()
