#!/usr/bin/env python

import socket
import threading 
import signal
import sys
import os

class WebServer:
	def __init__(self, port, ip):
		self.port = port
		self.ip = ip

	def StartServer(self):
		tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
		tcpSocket.bind(("127.0.0.1",1000))
		tcpSocket.listen(1)
		(clientFD, (ip, port)) = tcpSocket.accept()
		t = threading.Thread(target=self.handle,args = (clientFD, (ip,port)))
		t.start()

	def handle(self, clientFD, clientAddr):
		print "Connection Recieved form: " + "IP: " + str(clientAddr[0]) + "port:" + str(clientAddr[1])
        	try:
			data = clientFD.recv(2048)
			self.logfile(data)      
        		filename = data.split()[1]
			if filename[1:].find("/") != -1:
				self.displayDir(filename[1:],clientFD)
			else: 
				self.displayFile(filename[1:],clientFD)
        	except IOError:	
			clientFD.send("""<html>
			<head>
			<title>File not found</title>
			</head>
			<body>
			404 Bad Request
			</body>
			</html>
			""") 
			clientFD.close()
	def logfile(self, data):
		print data
		logfile = open("log.txt", "a")
		logfile.write("\n")
		logfile.write(data)
		logfile.close()
	
	def displayDir(self, dirname, clientFD):
		print "found directory"
		dir_list = os.listdir("/Users/meraj0/Desktop/PentestingAcademy - Web Application/PentestingPython/" + dirname)
		listing = "<br>"
		for filename in dir_list:
			listing = listing + "<a href="+dirname+filename+" download>"
		clientFD.send("""<html>
                        <head>
                        <title>Directory</title>
                        </head>
                        <body>"""
                        +listing+
                        """ </body>
                        </html>
                        """)
		
	def displayFile(self, filename, clientFD):
		f = open(filename)
                outputData = f.read()
                f.close()
                clientFD.send(outputData)
                clientFD.close()

while True:
	server = WebServer("1000","127.0.0.1")
	try:
		server.StartServer()
	except KeyboardInterrupt:
		print "exit"
		sys.exit()
