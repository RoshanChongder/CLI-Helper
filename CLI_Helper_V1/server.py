import socket
import sys

class Socket :
    def __init__(self,ip_add,port_num):
        try :
            self.ip = ip_add
            self.port = port_num
            self.s = socket.socket()
        except socket.error as msg :
            print("socket Creation failed : "+msg)
            sys.exit(1)
    #binding the port to the socket and listing to the port for request
    def bind_socket(self):
        try :
            print("Binding the id and port with the socket.")
            self.s.bind(( self.ip , self.port ))
            print("Binding successful.")
            self.s.listen(5)  # upto 5 request
            print("Port has started listening . . . .")
        except socket.error as msg:
            print("Socket binding failed to port num "+str(self.port))
            print("Try again by changing the port number .")
            sys.exit(1)
            #self.bind_socket()
    #accepting the request from the client
    #send commands to the client
    def socket_accept(self):
        connection,add=self.s.accept()
        print("Request is accepted from the clinet "+ add[0])
        self.send_commands(connection)
        connection.close()
    def send_commands(self,conn):
        while True :
            x = str(conn.recv(1024), "utf-8")
            print( x , end=" ")
            cmd=input()  # taking the command from the serverside user
            while (len(cmd)== 0 ) :
                print(x)
                cmd = input()
            if (cmd=='quit') :
                conn.close()
                self.s.close()
                sys.exit(1)
            elif len(cmd) > 0 :
                conn.send(str.encode(cmd)) # it will reply the op adter cmd is executed
                client_responce = str(conn.recv(1024),"utf-8") # as the received data is in byte format
                print(client_responce,end="\n")



#s = Socket("172.16.29.27",12345)
s = Socket("127.0.0.1",22345)
s.bind_socket()
s.socket_accept()

