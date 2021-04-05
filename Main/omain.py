import time
from threading import Thread
import random
import datetime
from logger import LC
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
    max_hr = 80
    min_hr = 60


    def compare(self, det_hr):
        self.alert()
        #calculate difference in set heart rate and detected heart rate
        dif_hr = (self.set_hr - det_hr)
        #calculates the time needed between each manual pulse
        if (det_hr != 60) & (dif_hr > 0):
            Main.pulse_interval = abs(1 / (1 - (det_hr / self.set_hr)))
            #print("Difference in HR", dif_hr)
            #print("Pulse Interval:", Main.pulse_interval)
        time.sleep(2)

    def pulse(self):
        #print("pulse Starting")
        #time.sleep(5)
        while True:
            #print(self.pulse_interval)
            time.sleep(Main.pulse_interval)
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Pulse!!!!!!")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !!!!!!Pulse!!!!!!")
            HR_Detection.avghr()
            self.clock()

    def alert(self):
        alert = ""
        if (HR_Detection.rhr < self.min_hr):
            alert = "LOW"
            #print(f"Heart Rate Alert: {alert}")
        if (HR_Detection.rhr  > self.max_hr):
            alert = "HIGH"
            #print(f"Heart Rate Alert: {alert}")
        else:
            return



    def clock(self):
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print("Current Time: ", result)
        print("-----------------------------")

class HR_Detection():
    hr = 50
    rhr = 0
    def avghr():
        #creates a random int in range of 40-80 as an average heart rate
        r = random.randrange(-10, 10)
        HR_Detection.rhr = (HR_Detection.hr + r)
        #print(HR_Detection.rhr)
        #print("Random hr:", rhr)
        #pushes the random heart rate to the compare function in the main calss
        ppm_main.compare(HR_Detection.rhr)
        #time.sleep(5)

    def heart():
        while True:
            time.sleep(HR_Detection.rhr/60)
            time.sleep(20)
            print("BEAT")


#def tik():




ppm_main = Main()
#ppm_hr_det = HR_Detection()

#ppm.compare(50)

Thread(target=ppm_main.pulse).start()
#Thread(target=HR_Detection.heart()).start()
#Thread(target=ppm_main.clock("start")).start()
#Thread(target=ppm_hr_det.avghr()).start()



