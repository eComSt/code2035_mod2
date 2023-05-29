import socket
from threading import Thread

HOST = "0.0.0.0"
PORT = 5002

clients_sockets = set()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(5)
print(f"[*] listen {HOST}:{PORT}")

def listen_for_client(cs):
	while True:
		try:
			msg= cs.recv(1024).decode()
			for c in clients_sockets:c.send(msg.encode())
		except:clients_sockets.remove(cs)
while True:
	client_socket, client_address = s.accept()
	print(f"[+] {client_address} connected")
	clients_sockets.add(client_socket)
	t = Thread(target = listen_for_client, args = (client_socket,))
	t.daemon = True
	t.start()
for cs in clients_sockets:
	cs.close()
s.socket()