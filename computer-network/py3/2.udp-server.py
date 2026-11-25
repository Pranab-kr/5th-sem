# Title: UDP Server (Python 3)
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print("UDP Server listening on port 12345...")

data, addr = server_socket.recvfrom(1024)
print("Received from client:", data.decode())

server_socket.sendto("Hello from UDP Server!".encode(), addr)

# Example Output:
# UDP Server listening on port 12345...
# Received from client: Hello from UDP Client!