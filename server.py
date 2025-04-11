import socket
import os

HOST = '192.168.47.129'  # Change this to '127.0.0.1' if running on the same machine
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    file_name = conn.recv(1024).decode().strip()
    if not file_name:
        print("No file name received.")
        conn.close()
        continue

    file_size = conn.recv(1024).decode().strip()
    if not file_size.isdigit():
        print("Invalid file size received.")
        conn.close()
        continue

    file_size = int(file_size)
    print(f"Receiving file: {file_name} ({file_size} bytes)")

    with open(file_name, 'wb') as file:
        received_bytes = 0
        while received_bytes < file_size:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
            received_bytes += len(data)

    print(f"File '{file_name}' received successfully!")
    conn.close()
