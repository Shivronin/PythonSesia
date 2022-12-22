import os
import multiprocessing as mp
import asyncio
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('localhost',9990))

# server_socket.send("hello, world!".encode())
# data = server_socket.recv(1024).decode('utf-8')
# server_socket.close()
# print(data)
        
print("Введите информацию или команду")
while True:
    data = input()
    if(data != ""):
        lenght = len(data.encode())
        server_socket.send((str(lenght) + " " + data).encode())