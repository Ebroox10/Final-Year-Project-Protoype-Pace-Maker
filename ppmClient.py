import socket

host = '127.0.0.1'
port = 1234
#host = input("Please Enter Host Address: ")
#port = input("Please Enter Host Port: ")
#print(host, port)

def out(msg):
    msg = msg.encode("utf-8")
    s.sendall(msg)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    sid = s.recv(1024).decode('utf-8')
    print(f"Connected to server: {sid}")
    input("press any key to continue")
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