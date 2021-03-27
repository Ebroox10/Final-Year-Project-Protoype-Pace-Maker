class SysAdmin():
    maxhr = 92
    minhr = 52
    avghr = 72
    def setmaxhr(option):         #This is the maximum heart rate that triggers a high alert
        SysAdmin.maxhr = option
        PaceWall.maxhrchk()

    def setminhr(option):         #This is the minum heart rate that triggers a low alert
        SysAdmin.minhr = option
        PaceWall.minhrchk()


    def setavghr(option):         # This function determins what bpm the program will attempt to keep average
        SysAdmin.avghr = option
        PaceWall.avghrchk()

class PaceWall():                       #this function acts as the firewall for the pacemaker preventing malicious variabels being set eg. "avghr = 1000"
    pw_maxhr = 100
    pw_minhr = 40                       # Incorporation of these varaibles to a readonly file
    pw_maxavghr = 90
    pw_minavghr = 50

    def maxhrchk():
        if (SysAdmin.maxhr <= PaceWall.pw_maxhr):
            print(f"Setting MaxHR to {SysAdmin.maxhr}")
        else:
            print(f"ERROR: The MaxHR of {SysAdmin.maxhr} is too big, MaxHR allowed on this system is {PaceWall.pw_maxhr}.")

    def minhrchk():
        if (SysAdmin.mihr >= PaceWall.pw_minhr):
            print(f"Setting MaxHR to {SysAdmin.minhr}")
        else:
            print(f"ERROR: The MaxHR of {SysAdmin.minhr} is too big, MaxHR allowed on this system is {PaceWall.pw_maxhr}.")


    def avghrchk():
        if (PaceWall.pw_minavghr <= SysAdmin.avghr <= PaceWall.pw_maxavghr):
            print(f"Setting AvgHR to {SysAdmin.avghr}")
        else:
            print(f"ERROR: The AvgHR of {SysAdmin.avghr} is out of range, the allowed range on this system is {PaceWall.pw_minavghr} - {PaceWall.pw_maxavghr}.")
