from main import Main
import datetime
from csv import reader, register_dialect
import os
from Crypto.Hash import SHA256
register_dialect('udata', delimiter='|')
startuptime = datetime.datetime.now()
class SysAdmin():
    maxhr = 92
    minhr = 52
    avghr = 72
    userdata = []
    def setmaxhr(option):         #This is the maximum heart rate that triggers a high alert
        SysAdmin.maxhr = option
        out = PaceWall.maxhrchk()
        return out

    def setminhr(option):         #This is the minum heart rate that triggers a low alert
        SysAdmin.minhr = option
        out = PaceWall.minhrchk()
        return out



    def setavghr(option):         # This function determins what bpm the program will attempt to keep average
        SysAdmin.avghr = option
        out = PaceWall.avghrchk()
        return out

    def chkinfo():
        info = f"|Current set HR: {Main.set_hr}|Current Max HR {Main.max_hr}|Current Min HR {Main.min_hr}|Current Pulse intv {Main.pulse_interval}|"
        return info

    def loaduserdata():
        with open('userdata.csv', 'r') as ud:
            SysAdmin.userdata = dict(reader(ud, 'udata'))

    def delusr(option):
        found = False
        with open('userdata.csv', 'r') as ud:
            userdata = dict(reader(ud, 'udata'))
        for users in userdata:
            if option == users:
                os.remove('userdata.csv')
                found = True
                break;

        if found:
            del userdata[option]
            with open('userdata.csv', 'wb') as ud:
                for key in userdata.keys():
                    ud.write((f"{key}|{userdata[key]}\n").encode('utf-8'))
                    out = f"User {option} Deleted"
                    SysAdmin.loaduserdata()
            return out
        if not found:
            out = f"User {option} Was not Found"
            return out

    def addusr(uname, passwd):
        hpasswd = (SHA256.new(passwd.encode('utf-8'))).digest()
        SysAdmin.userdata.update({uname:hpasswd})
        os.remove('userdata.csv')
        with open('userdata.csv', 'wb') as ud:
            for key in SysAdmin.userdata.keys():
                ud.write((f"{key}|{SysAdmin.userdata[key]}\n").encode('utf-8'))
                out = f"User {uname} Added"
        SysAdmin.loaduserdata()
        return out

    def chkusr():
        out = '\n'.join(f'{key}' for key, value in SysAdmin.userdata.items())
        return out

    def chkuptime():
        #out = f"Uptime is {}"
        out =  f"Uptime: {((datetime.datetime.now()) - (startuptime)).days}"
        return out








            #userdata_read = reader(userdata)
            #list_of_userdata = list(userdata_read)
            #print(list_of_userdata)







class PaceWall():                       #this function acts as the firewall for the pacemaker preventing malicious variabels being set eg. "avghr = 1000"
    pw_maxhr = 100
    pw_minhr = 40                       # Incorporation of these varaibles to a readonly file
    pw_maxavghr = 90
    pw_minavghr = 50

    def maxhrchk():
        if (SysAdmin.maxhr <= PaceWall.pw_maxhr):
            Main.max_hr = SysAdmin.maxhr
            return True

        else:
            return False


    def minhrchk():
        if (SysAdmin.minhr >= PaceWall.pw_minhr):
            Main.min_hr = SysAdmin.minhr
            return True
        else:
            return False

    def avghrchk():
        if (PaceWall.pw_minavghr <= SysAdmin.avghr <= PaceWall.pw_maxavghr):
            Main.set_hr = SysAdmin.avghr
            return True
        else:
            return False


#SysAdmin.setminhr(0)
SysAdmin.loaduserdata()