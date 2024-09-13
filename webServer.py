#reference material:
#https://www.geeksforgeeks.org/socket-programming-python/
#https://docs.python.org/3/library/socket.html#socket.socket.listen
#https://realpython.com/python-sockets/#echo-server

#Total points awarded: 60.0
#Test score (ok in message) points awarded: 15/15
#Test score (200 in message) points awarded: 15/15
# TODO Test score (html body content found in message) points awarded: 0/15
# TODO Test score (404 in message) points awarded: 0/15
# TODO Test score (headers found in message) points awarded: 5/15
#Test score (status line comes first) points awarded: 12.5
#Test score (headers come before response body) points awarded: 12.5

# import socket module
 # In order to terminate the program
import sys
from socket import *


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  # listen 1 - handles ONE HTTP req at a time
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end
      filename = message.split()[1]
      #get message
      #print(message)
      #print(message.split()[1]) --> /helloworld.html

      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:])#,  #fill in start #fill in end)

      #filename logic
      if filename == "/helloworld.html":
        f = open(filename[1:], "r")
        outputdata = f.read()
      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      #outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"

        #connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        #connectionSocket.send(b"Content-Type: text/html; charset=UTF-8\r\n")

        connectionSocket.send("HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\r\n\r\n".encode())

      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
        #connectionSocket.send("\r\n\r\n".encode())
      #Fill in end
               
        #for i in f: #for line in file
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())
      #Fill in start - append your html file contents #Fill in end
        connectionSocket.send(b"\r\n")
        f.close()
      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      # TODO - missing something?
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      #print("exception occured")
      #print(e)

      #print("404 Not Found")
      # need to send all at once
      connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

      #connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
