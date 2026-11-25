# Title: TCP Client (Python 3)
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.send("Hello from TCP Client!".encode())
data = client_socket.recv(1024).decode()
print("Received from Server:", data)
client_socket.close()

# Example Output:
# Received from Server: Hello from Server!