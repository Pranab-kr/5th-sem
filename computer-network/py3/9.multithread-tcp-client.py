# Title: Multithreaded TCP Client (Python 3)
import socket

def start_client(host='127.0.0.1', port=5000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print("[CLIENT] Connected to the server.")
    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        client.send(msg.encode())
        response = client.recv(1024).decode()
        print(f"[SERVER REPLY]: {response}")
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