# Title: Multithreaded TCP Server (Python 3)
import socket
import threading

def handle_client(client_socket, address):
    print(f"[+] New connection from {address}")
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"[{address}] {data}")
            client_socket.send(f"Message received: {data}".encode())
        except:
            break
    print(f"[-] Connection closed: {address}")
    client_socket.close()

def start_server(host='127.0.0.1', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[SERVER] Listening on {host}:{port}")
    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()

# Example Output:
# [SERVER] Listening on 127.0.0.1:5000
# [+] New connection from ('127.0.0.1', 54321)
# [ACTIVE CONNECTIONS] 1
# [('127.0.0.1', 54321)] Hello Server
# [('127.0.0.1', 54321)] How are you?
# [-] Connection closed: ('127.0.0.1', 54321)