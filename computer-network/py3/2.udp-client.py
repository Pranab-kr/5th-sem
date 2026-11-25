# Title: UDP Client (Python 3)
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("Hello from UDP Client!".encode(), ('localhost', 12345))
data, addr = client_socket.recvfrom(1024)
print("Received from Server:", data.decode())
client_socket.close()

# Example Output:
# Received from Server: Hello from UDP Server!