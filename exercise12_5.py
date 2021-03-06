"""
Exercise  12.4: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember that
recv is receiving characters (newlines and all), not lines.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 5, 2017
"""
import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   #Finds the end of header
                                            #Adds four to exclude:'\r\n\r\n' 
print(message[header_end_pos:])             
while True:                                 #Header in the first data only
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()