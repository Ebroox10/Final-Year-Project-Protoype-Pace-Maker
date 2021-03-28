import socket
from SysAdmin import *
host = '127.0.0.1'
port = 1234

def switch(data):
    data = data.decode('utf-8')
    msg = ''

    if 'set minhr' in data:
        chk = SysAdmin.setminhr(int(data[10:]))
        if chk == True:
            msg = f"MinHR has been set to: {data[10:]}".encode('utf-8')

        else:
            msg =f"MinHR must be more than {PaceWall.pw_minhr}".encode('utf-8')
        conn.sendall(msg)
        return

    if 'set maxhr' in data:
        chk = SysAdmin.setmaxhr(int(data[10:]))
        if chk == True:
            msg = f"MaxHR has been set to: {data[10:]}".encode('utf-8')

        else:
            msg = f"MaxHR must be less than {PaceWall.pw_maxhr}".encode('utf-8')
        conn.sendall(msg)
        return

    if 'set avghr' in data:
        chk = SysAdmin.setavghr(int(data[10:]))
        if chk == True:
            msg = f"AvgHR has been set to: {data[10:]}".encode('utf-8')

        else:
            msg = f"AvgHR must be in the range {PaceWall.pw_minavghr} - {PaceWall.pw_maxavghr}".encode('utf-8')
        conn.sendall(msg)
        return

    if 'chkinfo' in data:
        msg = SysAdmin.chkinfo().encode('utf-8')
        conn.send(msg)
        return



    else:
        msg  = (f"---{data}--- IS AN INVALID COMMAND").encode('utf-8')
        conn.sendall(msg)

        return

while True:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            msg = "Prototype PaceMaker".encode('utf-8')
            conn.sendall(msg)
            while True:
                try:
                    data = conn.recv(1024)
                except:
                    print("Lost Connection to client")
                    break
                if not data:
                    break
                switch(data)