import socket
from AES import ECB
import os
host = '127.0.0.1'
port = 1235
epass = "9876"
#host = input("Please Enter Host Address: ")
#port = input("Please Enter Host Port: ")
#print(host, port)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print(f"Connected To: {ECB.decrypt(s.recv(1024).decode('utf-8'), epass)}")
    #sid = s.recv(1024).decode('utf-8')
    #print(f"Connected To: {sid}")
    login = True
    while login:
        uname = input("Enter UserName: ")
        s.sendall((ECB.encrypt(uname, epass)).encode('utf-8'))
        data = ECB.decrypt(s.recv(1024).decode('utf-8'), epass)
        if data == "True":
            pwd = input("Enter Password: ")
            s.sendall((ECB.encrypt(pwd, epass)).encode('utf-8'))
            data = ECB.decrypt(s.recv(1024).decode('utf-8'), epass)
            if data == "True":
                print(ECB.decrypt(s.recv(1024).decode('utf-8'), epass))
                login = False


            else:
                print("Invalid Password")
        else:
            print("INVALID USERNAME")






    while True:
        msg = input("Enter Text to send: ")

        if msg == "exit":
            print("quiting")
            quit()

        if msg == "":
            print("INVALID COMMAND")

        if msg == "cls":
            os.system('cls')

        else:
            s.sendall((ECB.encrypt(msg, epass)).encode('utf-8'))
            data = ECB.decrypt(s.recv(1024).decode('utf-8'), epass)
            if not data:
                break
            print(data)
