import psycopg2
from datetime import datetime
import binascii
import _thread
import time
import socket

PORT1 = 887
 
conn = psycopg2.connect(host="131.180.165.7",database="CRoF",user="postgres", password="crpg")


cursor = conn.cursor()
cursor.execute('''SELECT value from objects WHERE id=51''')
result = cursor.fetchone()
record1 = result[0]
cursor.execute('''SELECT value from objects WHERE id=52''')
result = cursor.fetchone()
record2 = result[0]

# Define a function for the thread
def server07():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
        s1.bind(('',PORT1))
        s1.listen()
        conn1, addr = s1.accept()
        with conn1:
            print('Server 1 from:',addr)
            while True:
                a = 1
                while a < 6:
                    cursor.execute('''SELECT value from objects WHERE id=51''')
                    result = cursor.fetchone()
                    if record1 != result[0]:
                        print(result[0])
                        string = "mu01"+str(result[0])
                        datax = string.encode()
                        s1.sendall(datax)
                        print(string)
                        record1 = result[0]

                    cursor.execute('''SELECT value from objects WHERE id=52''')
                    result = cursor.fetchone()
                    if record2 != result[0]:
                        print(result[0])
                        string = "mu01"+str(result[0])
                        datax = string.encode()
                        s1.sendall(datax)
                        print(string)
                        record2 = result[0]



try:                   
    _thread.start_new_thread( server07, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass

