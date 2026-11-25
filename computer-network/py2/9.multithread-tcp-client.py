# Title: Multithreaded TCP Client (Python 2)
import socket

def start_client(host='127.0.0.1', port=5000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print "[CLIENT] Connected to the server."
    while True:
        msg = raw_input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client.send(msg)
        response = client.recv(1024)
        print "[SERVER REPLY]: {}".format(response)
    client.close()

if __name__ == "__main__":
    start_client()

# Example Output:
# [CLIENT] Connected to the server.
# Enter message (type 'exit' to quit): Hello Server
# [SERVER REPLY]: Message received: Hello Server
# Enter message (type 'exit' to quit): How are you?
# [SERVER REPLY]: Message received: How are you?
# Enter message (type 'exit' to quit): exit