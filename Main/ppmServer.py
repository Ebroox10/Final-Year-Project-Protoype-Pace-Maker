import socket
import datetime
from SysAdmin import *
from Crypto.Hash import SHA256
from AES import ECB
from logger import LC
host = '127.0.0.1'
port = 1235
epass = "9876"  #change this to non hardcoded

class server():

    #def conchk():


    def switch(data):
        msg = ''

        if 'set minhr' in data:
            chk = SysAdmin.setminhr(int(data[10:]))
            if chk == True:
                result = f"MinHR has been set to: {data[10:]}".encode('utf-8')

            else:
                result = f"MinHR must be more than {PaceWall.pw_minhr}".encode('utf-8')
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'set maxhr' in data:
            chk = SysAdmin.setmaxhr(int(data[10:]))
            if chk == True:
                result = f"MaxHR has been set to: {data[10:]}".encode('utf-8')

            else:
                result = f"MaxHR must be less than {PaceWall.pw_maxhr}".encode('utf-8')
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'set avghr' in data:
            chk = SysAdmin.setavghr(int(data[10:]))
            if chk == True:
                result = f"AvgHR has been set to: {data[10:]}"

            else:
                result = f"AvgHR must be in the range {PaceWall.pw_minavghr} - {PaceWall.pw_maxavghr}"
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            log = open("Log.txt", "a")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))
            return

        if 'chkinfo' in data:
            result = SysAdmin.chkinfo()
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            log = open("Log.txt", "a")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'chkusr' in data:
            result = SysAdmin.chkusr()
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'delusr' in data:
            result = SysAdmin.delusr(data[7:])
            conn.sendall((ECB.encrypt(result, epass).encode('utf-8')))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'addusr' in data:
            sdata = data[7:].rsplit(sep=' ')
            result = SysAdmin.addusr(sdata[0], sdata[1])
            conn.sendall((ECB.encrypt(result, epass).encode('utf-8')))
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}")
            return

        if 'chkuptime' in data:
            conn.sendall((ECB.encrypt(SysAdmin.chkuptime(), epass).encode('utf-8')))
            return




        else:
            result = (f"---{data}--- IS AN INVALID COMMAND")
            logtxt = f":{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {(len(uname) * ' ')}->{result}"
            LC.log(logtxt)
            conn.sendall((ECB.encrypt(result, epass)).encode('utf-8'))

            return


LC.log(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  SERVER STARTING")



while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Connected by {addr}"
            print(logtxt)
            LC.log(logtxt)
            msg = "PaceWall SysAdmin"
            conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
            login = True
            SysAdmin.loaduserdata()
            connected = True
            while connected:
                while login:

                    try:
                        data = ECB.decrypt(conn.recv(1024).decode('utf-8'), epass)
                    except:
                        s.close()
                        connected = False
                        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                        logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                        LC.log(logtxt)
                        break
                    if data in SysAdmin.userdata:
                        uname = data
                        conn.sendall((ECB.encrypt("True", epass)).encode('utf-8'))
                        try:
                            data = ECB.decrypt(conn.recv(1024).decode('utf-8'), epass)
                        except:
                            s.close()
                            connected = False
                            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                            logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                            LC.log(logtxt)
                            break


                        if str(f"{(SHA256.new(data.encode('utf-8'))).digest()}") == SysAdmin.userdata[uname]:
                            conn.sendall((ECB.encrypt("True", epass)).encode('utf-8'))
                            conn.sendall((ECB.encrypt((f"Welcome To PaceWall: {uname}"), epass)).encode('utf-8'))
                            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname} has logged on")
                            logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname} has logged on"
                            LC.log(logtxt)
                            login = False

                        else:
                            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !ALERT!{addr}->###### INVALID PASSWORD")
                            logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !ALERT!{addr}->###### INVALID PASSWORD"
                            LC.log(logtxt)
                            try:
                                conn.sendall((ECB.encrypt("False", epass)).encode('utf-8'))
                            except:
                                s.close()
                                connected = False
                                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                                logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                                LC.log(logtxt)
                                break

                    else:
                        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !ALERT!{addr}->{data} INVALID USERNAME")
                        logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  !ALERT!{addr}->{data} INVALID USERNAME"
                        LC.log(logtxt)
                        try:
                            conn.sendall((ECB.encrypt("False", epass)).encode('utf-8'))
                        except:
                            s.close()
                            connected = False
                            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                            logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                            LC.log(logtxt)
                            break


                try:
                    data = ECB.decrypt((conn.recv(1024)).decode('utf-8'), epass)
                except:
                    s.close()
                    if login == False:
                        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                        logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                        LC.log(logtxt)
                    connected = False
                    break
                if not data:
                    try:
                        conn.sendall((ECB.encrypt("INVALID COMMAND", epass)).encode('utf-8'))
                    except:
                        s.close()
                        connected = False
                        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}")
                        logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  Lost Connection to {addr}"
                        LC.log(logtxt)
                        break
                    connected = False
                    break

                if "addusr" in data:
                    temp = data.rsplit(sep=' ')
                    x = 6 * "#"
                    msg = (f"{temp[0]} {temp[1]} {x}")
                    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname}->{msg}")
                    logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname}->{msg}"
                    LC.log(logtxt)
                    server.switch(data)

                else:
                    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname}->{data}")
                    logtxt = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}:  {uname}->{msg}"
                    LC.log(logtxt)
                    server.switch(data)

