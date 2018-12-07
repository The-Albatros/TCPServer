#!/usr/bin/python
import sys
import os
import time
import socket 
import threading
import sys, traceback

if not os.getuid()==0:
    sys.exit("\33[31mYou Need Root Privilege To Run This Script\33[0m")

time.sleep(5)
print(" _____ ____ ____    ____        ")
print("|_   _/ ___|  _ \  / ___|  ___ _ ____   _____ _ __  ")
print("  | || |   | |_) | \___ \ / _ \ '__\ \ / / _ \ '__| ")
print("  | || |___|  __/   ___) |  __/ |   \ V /  __/ |    ")
print("  |_| \____|_|     |____/ \___|_|    \_/ \___|_|   ")
print("\33[31m     .:. TCP Server Coded BY Gersi Gazhdaj .:.\33[0m")
print("                                                              ")
print("                                                       ")
print("                                                       ")
choice = raw_input("\33[31m[*]\33[0m" "\33[33m Press Enter To Start The Server...\33[0m")
time.sleep(5)
print("\33[31m[*]\33[0m" "\33[33m Please Wait For The Server...\33[0m")
time.sleep(5)
print("\33[31m[*]\33[0m" "\33[33m Checking Connection...\33[0m")
time.sleep(5)
print("\33[31m[*]\33[0m" "\33[33m Starting Server...\33[0m")
time.sleep(5)
bind_ip   = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)


print "\33[31m[*]\33[0m" "\33[33m Listening on :\33[0m" "\33[31m%s:%d\33[0m" % (bind_ip,bind_port)
print("")
print("")
  
# this is our client-handling thread
def handle_client(client_socket) :

   # print out what the client sends 
   request = client_socket.recv(1024)

   print "[*] Received: %s" % request

   # send back a packet
   client_socket.send("ACK!")

   client_socket.close()


while True:

    client,addr = server.accept()
print "\33[31m[*]\33[0m" "\33[33m Accepted connection from: \33[0m" "\33[31m%s:%d\33[0m" % (addr[0],addr[1])


# spin up our client thread to handle incoming data 
client_handler = threading.Thread(target=handle_client,args=(client,))
client_handler.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("interrupted")
        sys.exit(0)
    
