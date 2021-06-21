import time
from threading import Thread
import random
import datetime
from logger import LC
from time import sleep
#import RPi.GPIO as GPIO

#GPIO stuff
#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#PULSE = 35
#OHEART = 37
#PHEART = 33

#GPIO.setup(PULSE, GPIO.OUT)
#GPIO.setup(OHEART, GPIO.OUT)
#GPIO.setup(PHEART, GPIO.OUT)
#GPIO END

class Main():
    set_hr = 60                #change to import sysadmin variables passed through PaceWall
    pulse_interval = 3
    max_hr = 70
    min_hr = 40
    avghr = 0
    hrlist = [0,1,2,3,4]
    count = 0

    def pm(self):
        while True:
            #print("----------------------------")
            Heart.bps()
            self.avgcal()
            self.alert()
            if (Heart.bpm/60) < (self.set_hr/60):
                #Thread(target=Heart.beat()).start()
                sleep(60/Main.set_hr)
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Pulse!!!!!!")
                LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Pulse!!!!!!")
                #GPIO.output(PULSE, GPIO.HIGH)
                #GPIO.output(PHEART, GPIO.HIGH)
                #sleep(0.1)
                #GPIO.output(PULSE, GPIO.LOW)
                #GPIO.output(PHEART, GPIO.LOW)

            else:
                sleep(60/Heart.bpm)
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!HeartBeat!!!!!!")
                #GPIO.output(OHEART, GPIO.HIGH)
                #sleep(0.1)
                #GPIO.output(OHEART, GPIO.LOW)
            #print("--------------------------------")
    def alert(self):
        if (Heart.bpm < self.min_hr):
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Heart Rate LOW!!!!!!")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Heart Rate LOW!!!!!!")
        if (Heart.bpm > self.max_hr):
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Heart Rate HIGH!!!!!!")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Heart Rate HIGH!!!!!!")
        else:
            return

    def avgcal(self):
        #print("TEST")
        if self.count == 5:
            Main.avghr = (self.hrlist[0] + self.hrlist[1] + self.hrlist[2] + self.hrlist[3] + self.hrlist[4])/5
            #print (Main.hrlist)
            self.count = 0
            #print(Main.avghr)
        else:
            Main.hrlist[self.count] = Heart.bpm
            #print(self.hrlist)
            #print(self.count)
            self.count += 1

class Heart():
    rantime = 0
    bpm = 0
    hearthealth = 0 # 0-Healthy 1-slightissues 2-Ill 3-Death 4-sparatic
    def bps():

        if Heart.hearthealth == 0:
            Heart.rantime = random.uniform(1, 1)
        if Heart.hearthealth == 1:
            Heart.rantime = random.uniform(0.95, 1.10)
        if Heart.hearthealth == 2:
            Heart.rantime = random.uniform(0.95, 1.20)
        if Heart.hearthealth == 3:
            Heart.rantime = random.uniform(2, 2)
        if Heart.hearthealth == 4:
            Heart.rantime = random.uniform(0.90, 1.5)


        Heart.bpm = (60/Heart.rantime)

        #print(Heart.bpm)
        #print(Heart.rantime)
        #sleep(Heart.rantime)
    def beat():
        sleep(Heart.rantime)
        #print("SHEARTBEAT")
        #GPIO.output(OHEART, GPIO.HIGH)
        #GPIO.output(PHEART, GPIO.HIGH)
        #sleep(0.1)
        #GPIO.output(OHEART, GPIO.LOW)
        #GPIO.output(PHEART, GPIO.LOW)



#def tik():





#ppm_hr_det = HR_Detection()

#ppm.compare(50)
ppm_main = Main()
Thread(target=ppm_main.pm).start()
#Thread(target=HR_Detection.heart()).start()
#Thread(target=ppm_main.clock("start")).start()
#Thread(target=ppm_hr_det.avghr()).start()



