import socket
import os
import time

SERVER_IP = '192.168.47.129'
PORT = 5001

file_path = input("Enter the full file path to send: ")

if not os.path.exists(file_path):
   print("File does not exist.")
   exit()

file_name = os.path.basename(file_path)
file_size = os.path.getsize(file_path)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

client_socket.sendall(file_name.encode() + b'\n')
time.sleep(0.1)
client_socket.sendall(str(file_size).encode() + b'\n')
time.sleep(0.1)


with open(file_path, 'rb') as file:
   while ( data := file.read(1024)):
     client_socket.sendall(data)

print(f"File '{file_name}' sent successfully!")
client_socket.close()
