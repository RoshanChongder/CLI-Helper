import threading , os 
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
    def recv(conn,s):
        while True :
            x = str(conn.recv(3000),"utf-8")
            if str.lower(x) == 'quit' :
                print("Clinet has ended the chat .")
                break  
            print( s + " : " + x)
    @staticmethod
    def start(conn,s) :
        print("Chat Application : ")
        t1 = threading.Thread(target = chat.send,args=(conn,))
        t2 = threading.Thread(target = chat.recv ,args=(conn,s,))

        t1.start() # starting the thread for sending message
        t2.start() # starting the thread for receving the message
        t1.join()  # wait untill thread 1 ends 
        t2.join()  # wait untill thread 2 ends 
   