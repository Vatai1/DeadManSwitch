from tkinter import *
from time import time
from telethon import TelegramClient

api_id = 19235970
api_hash = '053b368ce3f09179fe82b1b9a5020092'

def clicked():
    return 0

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

window = Tk()
window.title("Dead Men Switch")
window.geometry('700x300')


lbl = Label(window, text="Dead Men Switch", font=("Times New Roman Bold", 50))
lbl.grid(column=0, row=0)

text = Entry();

btn_setTimer = Button(window, text='setTimer', command=)





window.mainloop()
