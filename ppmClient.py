import socket
host = '127.0.0.1'
port = 1235
#host = input("Please Enter Host Address: ")
#port = input("Please Enter Host Port: ")
#print(host, port)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    sid = s.recv(1024).decode('utf-8')
    print(f"Connected To: {sid}")
    login = True
    while login:
        uname = input("Enter UserName: ").encode('utf-8')
        s.sendall(uname)
        data = s.recv(1024)
        if data.decode('utf-8') == "True":
            pwd = input("Enter Password: ").encode('utf-8')
            s.sendall(pwd)
            data = s.recv(1024)
            if data.decode('utf-8') == "True":
                print(s.recv(1024).decode('utf-8'))
                login = False


            else:
                print("Invalid Password")
        else:
            print("INVALID USERNAME")






    while True:
        msg = input("Enter Text to send: ").encode('utf-8')

        if msg.decode('utf-8') == "exit":
            print("quiting")
            quit()

        s.sendall(msg)
        data = s.recv(1024)
        if not data:
            break
        print(data.decode('utf-8'))
