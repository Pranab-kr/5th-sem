# Title: Multithreaded TCP Server (Python 2)
import socket
import threading

def handle_client(client_socket, address):
    print "[+] New connection from {}".format(address)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print "[{}] {}".format(address, data)
            client_socket.send("Message received: {}".format(data))
        except:
            break
    print "[-] Connection closed: {}".format(address)
    client_socket.close()

def start_server(host='127.0.0.1', port=5000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print "[SERVER] Listening on {}:{}".format(host, port)
    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()
        print "[ACTIVE CONNECTIONS] {}".format(threading.active_count() - 1)

if __name__ == "__main__":
    start_server()

# Example Output:
# [SERVER] Listening on 127.0.0.1:5000
# [+] New connection from ('127.0.0.1', 54321)
# [ACTIVE CONNECTIONS] 1
# [('127.0.0.1', 54321)] Hello Server
# [('127.0.0.1', 54321)] How are you?
# [-] Connection closed: ('127.0.0.1', 54321)