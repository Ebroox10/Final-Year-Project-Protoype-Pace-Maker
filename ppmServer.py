import socket
from SysAdmin import *
from Crypto.Hash import SHA256
from AES import ECB
host = '127.0.0.1'
port = 1235
epass = "9876"  #change this to non hardcoded


def switch(data):
    msg = ''

    if 'set minhr' in data:
        chk = SysAdmin.setminhr(int(data[10:]))
        if chk == True:
            msg = f"MinHR has been set to: {data[10:]}".encode('utf-8')

        else:
            msg =f"MinHR must be more than {PaceWall.pw_minhr}".encode('utf-8')
        conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
        return

    if 'set maxhr' in data:
        chk = SysAdmin.setmaxhr(int(data[10:]))
        if chk == True:
            msg = f"MaxHR has been set to: {data[10:]}".encode('utf-8')

        else:
            msg = f"MaxHR must be less than {PaceWall.pw_maxhr}".encode('utf-8')
        conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
        return

    if 'set avghr' in data:
        chk = SysAdmin.setavghr(int(data[10:]))
        if chk == True:
            msg = f"AvgHR has been set to: {data[10:]}"

        else:
            msg = f"AvgHR must be in the range {PaceWall.pw_minavghr} - {PaceWall.pw_maxavghr}"
        conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
        return

    if 'chkinfo' in data:
        msg = SysAdmin.chkinfo()
        conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
        return



    else:
        msg  = (f"---{data}--- IS AN INVALID COMMAND")
        conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))

        return


while True:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            msg = "PaceWall SysAdmin"
            conn.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
            login = True
            SysAdmin.loaduserdata()
            while login:
                data = conn.recv(1024)
                if ECB.decrypt(data.decode('utf-8'), epass) in SysAdmin.userdata:
                    uname = ECB.decrypt(data.decode('utf-8'), epass)
                    conn.sendall((ECB.encrypt("True", epass)).encode('utf-8'))
                    data = conn.recv(1024)


                    if str((SHA256.new((ECB.decrypt(data.decode('utf-8'), epass)).encode('utf-8'))).digest()) == SysAdmin.userdata[uname]:

                        conn.sendall((ECB.encrypt("True", epass)).encode('utf-8'))
                        conn.sendall((ECB.encrypt((f"Welcome To PaceWall: {uname}"), epass)).encode('utf-8'))
                        login = False

                    else:
                        conn.sendall((ECB.encrypt("False", epass)).encode('utf-8'))

                else:
                    conn.sendall((ECB.encrypt("False", epass)).encode('utf-8'))

            while True:
                try:
                    data = ECB.decrypt((conn.recv(1024)).decode('utf-8'), epass)
                except:
                    print("Lost Connection to client")
                    break
                if not data:
                    break
                switch(data)
