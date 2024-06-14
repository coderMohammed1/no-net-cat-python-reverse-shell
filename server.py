import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.26" # change this (the ip that we are listening on)
port =  1234 # change this

serv.bind((host,port))
serv.listen() 

csoc, adder = serv.accept()
print(f"connected:{adder}")

while True:  
    command = input("command: ")  
    csoc.send(command.encode('utf-8'))  

    if command.lower() == "exit":  
        break

    message = csoc.recv(1024).decode('utf-8')
    print(f"the message: {message}")

csoc.close()
