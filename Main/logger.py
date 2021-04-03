from AES import ECB

class LC():
    sfcnt = 0
    epass = "9876"
    def log(data):
        logtxt = f"{LC.sfcnt}:{data}"
        log = open("Log.txt", "a")
        #print((ECB.encrypt(logtxt, epass)), file=log)
        print(logtxt, file=log)
        LC.sfcnt += 1
        log.close()
