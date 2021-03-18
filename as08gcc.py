import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.7.0.11'
HOST2 = '100.7.0.12'
HOST3 = '100.7.0.13'
HOST4 = '100.7.0.14'
HOST5 = '100.7.0.15'
HOST6 = '100.7.0.16'
HOST7 = '100.7.0.17'
HOST8 = '100.7.0.18'
HOST9 = '100.7.0.19'
HOST10 = '100.7.0.20'
RHOST = '131.180.165.21'

PORT2 = 993
PORTS2 = 887



# Define a function for the thread
def serverOne():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
        sc1.connect((HOST1, PORT2))
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc2:
            sc2.connect((HOST2, PORT2))
             
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc3:
                sc3.connect((HOST3, PORT2))
                
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc4:
                    sc4.connect((HOST4, PORT2))
                    
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc5:
                        sc5.connect((HOST5, PORT2))

                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sr:
                            sr.connect((RHOST,PORTS2))
                            #sr.listen()
                            #conn2, addr2 = sr.accept()
                            with sr:
                                print('S2 from:',addr2)
                                while True:
                                    b = 1
                                    while b < 6:
                                    #recive data from server A
                                    data2 = sr.recv(1024)
                                    data2new = data2.decode("utf-8")
                                    if 'mu01' in data2new:
                                        part1,part2 = data2new.split("_")
                                        print(part2)
                                        part2x = part2.encode()
                                        #sc1.sendall(part2x)
                                    elif 'mu02' in data2new:
                                        part1,part2 = data2new.split("_")
                                        print(part2)
                                        part2x = part2.encode()
                                        #sc2.sendall(part2x)
                                    elif 'mu03' in data2new:
                                        part1,part2 = data2new.split("_")
                                        print(part2)
                                        part2x = part2.encode()
                                        #sc3.sendall(part2x)
                                    elif 'mu04' in data2new:
                                        part1,part2 = data2new.split("_")
                                        print(part2)
                                        part2x = part2.encode()
                                        #sc4.sendall(part2x)
                                    elif 'mu05' in data2new:
                                        part1,part2 = data2new.split("_")
                                        print(part2)
                                        part2x = part2.encode()
                                        #sc5.sendall(part2x)
                                    else:
                                        print(".")

                                            
                                            
							
# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass