# Title: TCP Server (Python 3)
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("TCP Server listening on port 12345...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

data = conn.recv(1024).decode()
print("Received from client:", data)
conn.send("Hello from Server!".encode())
conn.close()

# Example Output:
# TCP Server listening on port 12345...
# Connection from ('127.0.0.1', 35086)
# Received from client: Hello from TCP Client!