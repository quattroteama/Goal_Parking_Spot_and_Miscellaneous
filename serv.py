import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
server_address2 = (server_name, 20000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

sock2.bind(server_address2)
sock2.listen(1)

#while True:
connection, client_address = sock.accept()
f1 = open('map.pgm','r') 
l1 = f1.read(1024)
while (l1):
       	connection.send(l1)
       	l1 = f1.read(1024)
f1.close()
connection.close()

connection2, client_address2 = sock2.accept()
f2 = open('goalCoordinate.txt','r') 
l2 = f2.read(1024)
while (l2):
       	connection2.send(l2)
       	l2 = f2.read(1024)
f2.close()
connection2.close()

sock.close()
sock2.close()
