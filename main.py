import time
from threading import Thread
import random

class Main():
    set_hr = 60
    pulse_interval = 3

    def compare(self, det_hr):
        #calculate difference in set heart rate and detected heart rate
        dif_hr = (self.set_hr - det_hr)
        #calculates the time needed between each manual pulse
        if (det_hr != 60) & (dif_hr > 0):
            self.pulse_interval = abs(1 / (1 - (det_hr / self.set_hr)))
            print("Difference in HR", dif_hr)
            print("Pulse Interval:", self.pulse_interval)
        time.sleep(2)

    def pulse(self):
        print("pulse Starting")
        time.sleep(5)
        while True:
            #print(self.pulse_interval)
            time.sleep(self.pulse_interval)
            print("!!!!!!Pulse!!!!!!")

    def clock(self):
        while True:
            localtime = time.localtime()
            result = time.strftime("%I:%M:%S %p", localtime)
            print("Current Time: ", result)
            print("-----------------------------")
            time.sleep(1)

class HR_Detection():
    hr = 50
    def avghr(self):
        while True:
            #creates a random int in range of 40-80 as an average heart rate
            r = random.randrange(-1, 1)
            rhr = (self.hr + r)
            #print("Random hr:", rhr)
            #pushes the random heart rate to the compare function in the main calss
            ppm_main.compare(rhr)
            time.sleep(5)





ppm_main = Main()
ppm_hr_det = HR_Detection()

#ppm.compare(50)
Thread(target=ppm_main.pulse).start()
Thread(target=ppm_main.clock).start()
Thread(target=ppm_hr_det.avghr()).start()



