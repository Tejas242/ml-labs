import socket
import threading

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"\nServer: {msg}")
        except:
            break

def send(sock):
    while True:
        msg = input("You: ")
        sock.send(msg.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

threading.Thread(target=receive, args=(client,), daemon=True).start()
threading.Thread(target=send, args=(client,), daemon=True).start()

while True:
    pass 
