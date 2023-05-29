import socket
import threading

HOST = '51.250.65.169'  # The server's hostname or IP address
PORT = 5002
s = socket.socket()
s.connect((HOST, PORT))
print(f"[+] Connected")
name = input("Enter your name: ")
def listen():
    while True:
        try:
            data = s.recv(1024)
            print("\n"+data.decode('utf-8'))
        except:pass
t = threading.Thread(target=listen)
t.daemon = True
t.start()
while True:
    msg = input("")
    if msg == "exit":
        break
    msg = name + ": " + msg
    s.send(msg.encode('utf-8'))
s.close()