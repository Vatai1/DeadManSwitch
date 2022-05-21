from telethon import TelegramClient
from time import time


class DeadMen:

    def __init__(self, contacts=None, deadTime=172800):  # 172800 seconds = 2 days

        if contacts is None:
            self.contacts = ['me']
        else:
            self.contacts = contacts
        if deadTime is None:
            self.deadTime = 5
            self.timeStart = time()
            self.timeEnd = time() + 5
        else:
            self.deadTime = deadTime
            self.timeStart = time()
            self.timeEnd = time() + deadTime

    def timerWait(self):
        while True:
            if time() > self.timeEnd:
                break

    def timerUpdate(self, deadTime):
        self.deadTime = deadTime
        self.timeStart = time()
        self.timeEnd = time() + deadTime

    def run(self):
        print(self.timeStart)
        print(self.timeEnd)
        print(self.deadTime)

        self.timerWait()
        self.sendDeadMessageTelegram()

    def sendDeadMessageTelegram(self):
        for i in self.contacts:
            with TelegramClient('anon', api_id, api_hash) as client:
                client.loop.run_until_complete(client.send_message(i, 'Чего делош?'))


deadMen = DeadMen(deadTime=5)
deadMen.run()
