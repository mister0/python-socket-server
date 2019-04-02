# load additional Python modules
import socket  
import time
import event_pb2

PORT = 23456

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the configured port  and connect
server_address = (ip_address, PORT)  
sock.connect(server_address)  

print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

# define example event to be sent to the server
event = event_pb2.EventProto()
event.timestamp = 1234567889
event.userId = 12345
event.event = "2 hours of downtime occurred due to the release of version 1.0.5 of the system"
new_data = event.SerializeToString()

# send to server
sock.sendall(new_data)

# close connection
sock.close()  