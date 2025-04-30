import socket
import threading

def receive(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(f"\nClient: {msg}")
        except:
            break

def send(client_socket):
    while True:
        msg = input("You: ")
        client_socket.send(msg.encode())


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)

print("Waiting for connection...")
client_socket, addr = server.accept()
print(f"Connected to {addr}")

threading.Thread(target=receive, args=(client_socket,), daemon=True).start()
threading.Thread(target=send, args=(client_socket,), daemon=True).start()

while True:
    pass
