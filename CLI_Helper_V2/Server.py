import socket , os 
import sys , talk
import threading 

class chat :
    
    # method to send and receive messages
    @staticmethod
    def send(conn) :
        try :
            print(" 'E' to exit and quit the chat before exiting . . .")
            while True :
                s = input()
                if s=='E' :
                    break  
                print("You : " + s)
                conn.send(str.encode(s))
            print("exiting the chat . Press enter ")
            input() # get hold the screen 
            os.system('cls')
        except : 
            print("some thing went wrong ")
    @staticmethod         
    def recv(conn):
        while True :
            x = str(conn.recv(3000),"utf-8")
            if str.lower(x) == 'quit' :
                print("Clinet has ended the chat .")
                break  
            print("client : "+x)
    @staticmethod
    def start(conn) :
        print("Chat Application : ")
        t1 = threading.Thread(target = self.send,args=(conn,))
        t2 = threading.Thread(target = self.recv ,args=(conn,))

        t1.start() # starting the thread for sending message
        t2.start() # starting the thread for receving the message
        t1.join()  # wait untill thread 1 ends 
        t2.join()  # wait untill thread 2 ends 
   


class Socket :
    # socket constructor 
    def __init__(self,ip_add,port_num):
        try :
            self.ip = ip_add
            self.port = port_num
            self.c = False
            self.s = socket.socket()
            self.conn_objects = []
            self.add = [] 
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
    #this thread will be running the server and accepting the clinets 
    def run_server(self):
        while True :
            try :
                connection,add=self.s.accept()
                self.s.setblocking(1)  # it mainly prevents from timeout 
                os.system('cls') # clearing the screen 
                print("Request is accepted from the clinet "+ add[0])
                self.conn_objects.append(connection)
                self.add.append(list(add))
                print( "successfully established with : " + add[0] )
                print("CLI helper >",end='')  # printing the teminal sign again 
            except  :
                print("Failed to accept client . " )

   
    # funt to show the clinet list 
    def client_list(self):
        j = 0 
        for i in self.add :
            print("Id : " + str(j+1) ,end='  ')
            print("client add :" + i[j][0])
            j+=1


    # starting communication with a client 
    def select(self , index ) :
        try :
            self.send_commands(self.conn_objects[index-1],index)
        except Exception as msg:
            print(msg)
            
   
    #this the thread which will run to control the connection 
    def controller(self) :
        while True :
            inst = input('CLI helper >')
            if len(inst)==0 :
                inst = input()
            try :
                if inst == 'ls' :
                    self.client_list ()
                elif 'select' in inst :
                    self.select( int( inst[len(inst)-1] ) )
                elif inst == 'quit' :
                    return 
                else :
                    print("No such commands are there : "+ inst )
            except Exception as e :
                print("Some thing went wrong :"+e)    

   
    #send commands to the client
    def send_commands(self,conn,id):
        if self.c ==False :
            talk.chat.start(conn,'Client')
            self.c = True 
        while True :
            x = str(conn.recv(5000), "utf-8")
            cmd=input("Id-" + str(id) +  x )  # taking the command from the serverside user
            if (cmd=='quit') :
                conn.close()
                self.s.close()
                return 
            elif cmd == 'CLI' :
                conn.send(str.encode( 'echo hold' )) 
                client_responce = str(conn.recv(5000),"utf-8") # as the received data is in byte format        
                return 
            elif len(cmd) > 0 :
                conn.send(str.encode(cmd)) # it will reply the op adter cmd is executed
                client_responce = str(conn.recv(5000),"utf-8") # as the received data is in byte format
                print(client_responce,end="\n")

   
   # runnung the whole programme 
    def run(self):
        t1 = threading.Thread(target = s.run_server)
        t2 = threading.Thread(target = s.controller)
        # starting the threads 
        t1.start()  # running the server 
        t2.start()  # running command line 
        # wait untill thread 1 and 2 ends 
        t1.join() 
        t2.join()


s = Socket("127.0.0.1",12345)
s.bind_socket()
s.run()  # base threading starting 
print("Exiting ")
