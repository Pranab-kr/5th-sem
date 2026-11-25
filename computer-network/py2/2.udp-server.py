# Title: UDP Server (Python 2)
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))
print "UDP Server listening on port 12345..."

data, addr = server_socket.recvfrom(1024)
print "Received from client:", data

server_socket.sendto("Hello from UDP Server!", addr)

# Example Output:
# UDP Server listening on port 12345...
# Received from client: Hello from UDP Client!