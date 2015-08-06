import socket

print "\nStarting Echo Server\n"
print "Waiting for clients too connect ..."

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#this will create tcp socket given IPv4 addresssing
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# allow socket resure if server terminates. Without this port will stall when terminiated
tcpSocket.bind(("127.0.0.1",8000)) 
tcpSocket.listen(2)#argument is number of concurent clients socket can handle 
(client, (ip, port)) = tcpSocket.accept() #tuple is needed. client refers to descriptor. Second is tuple of ip and client 
print "Recieved connection from: ", ip

client.send("Welcome to Echo Server\n") 

data = "dummy"
while len(data):
	data = client.recv(2048)#argument refers to length to accept
	print "Client Sent: " + data
	client.send(data)

print "\nShutting down Server" 
client.close()
tcpSocket.close()


