import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    print("Server started...")
    conn, addr = server.accept()
    print(f"Connected to {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Client:", data.decode())
        conn.sendall(data)
    conn.close()

if __name__ == "__main__":
    start_server()
