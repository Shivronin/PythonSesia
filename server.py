import asyncio
import socket
import os
from fileCode import Filecode
from typing import List
import re

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
list_result = []
def main ():
    server_socket.bind(('localhost',9990))
    server_socket.listen(0)
    asyncio.run(conn())

def input(str):
    with open ("test/test.txt", "w+") as file:
        file.write(str + "\n")

def reading(a):
    list_Imya = []
    list_result = []
    with open ("test/test.txt", "r+") as file:
            list_Imya.append(file.readline())
    list_command = a.split(" ")
    number = int(list_command[-1])
    if(list_command[-1] == "*"):
        return list_Imya
    elif(number > 0):
        n = 0
        while n != number:
            list_result.append(list_Imya[n])
            n+=1
        return list_result
    elif(number < 0):
        n = len(list_Imya)
        while n != number:
            list_result.append(list_Imya[n])
            n-=1
        return list_result

async def conn():
    loop = asyncio.get_event_loop()
    while True:
        print("[+] Waiting for incoming connections")
        cl_socket, remote_address = await loop.sock_accept(server_socket)
        command = (await loop.sock_recv(cl_socket, 1024)).decode('utf-8')
        await loop.sock_sendall(cl_socket, command.encode())
        print(command)
        path = os.path.join('.', 'test', 'test.txt')
        u = command
        if(u == "show data *" in command):
            print(list_result)
        elif(u == "show data"):
            input(command)
            replaced = re.sub('[\D]', '', u)
            list2 = open("test/test.txt", 'r+', encoding="UTF-8")
            e = list2.read().split('\n')
            list2.close()
            t = replaced
            # indexes = [i for i in range(int(t)-1)]
            # print([e[x] for x in indexes])
            print (t)
            
if __name__ == "__main__":
    main()
 


        #  list_chototam = reading(command)
        #             with open(path, "r+") as file:
        #                 read = file.readline() 