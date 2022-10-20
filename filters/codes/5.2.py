import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).


dst_ip = str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")









cachedic = {}


while True:
		c, addr = s.accept()
		print ('Got connection from', addr )
		cacherecvmsg = c.recv(1024).decode()
		#print('Server received '+recvmsg)
		#c.send('Hello client'.encode())
		
	 
		#Write your code here
		#1. Uncomment c.send 
		#2. Parse the received HTTP request
		#3. Do the necessary operation depending upon whether it is GET, PUT or DELETE
		#4. Send response
		##################
		
		#recvmsg = c.recv(1024).decode()
		
		clientrequest = cacherecvmsg.split()

		if(clientrequest[0]=="GET"):
			    key = clientrequest[1].split("=")

	        if key[len(key)-1] in cachedic.keys():
				res = 'HTTP/1.1 200 OK ' + serverdic[key[len(key)-1]] + '\r\n\r\n'
				c.send(res.encode())
			else:
                serverIP = "10.0.1.3"
                dst_ip = str(input("Enter dstIP: "))
                s = socket.socket()
                print(dst_ip)
                port = 12346
                s.connect((dst_ip, port))

                
                s.send(cacherecvmsg.encode())
                response = s.recv(1024).decode()
                # print(response)
                c.send(response.encode())
			
	
		elif(clientrequest[0]=="PUT"):
			        serverIP = "10.0.1.3"
                    dst_ip = str(input("Enter dstIP: "))
                    s = socket.socket()
                    print(dst_ip)
                    port = 12346
                    s.connect((dst_ip, port))


                    s.send(cacherecvmsg.encode())
                    response = s.recv(1024).decode()
                    #print(response)
                    c.send(response.encode())
			
		elif(clientrequest[0]=="DELETE"):
				key = clientrequest[1].split("/")
				

				if key[len(key)-1] in serverdic.keys():
					 del serverdic[key[len(key)-1]]
					 #res = 'HTTP/1.1 200 ok ' + 'deleated the key' + '\r\n\r\n' 
					 #c.send(res.encode())


					serverIP = "10.0.1.3"
                    dst_ip = str(input("Enter dstIP: "))
                    s = socket.socket()
                    print(dst_ip)
                    port = 12346
                    s.connect((dst_ip, port))


                    s.send(cacherecvmsg.encode())
                    response = s.recv(1024).decode()
                    # print(response)
                    c.send(response.encode())
			

				else:

					serverIP = "10.0.1.3"
                    dst_ip = str(input("Enter dstIP: "))
                    s = socket.socket()
                    print(dst_ip)
                    port = 12346
                    s.connect((dst_ip, port))


                    s.send(cacherecvmsg.encode())
                    response = s.recv(1024).decode()
                    #print(response)
			        c.send(response.encode())








c.close()



















import numpy as np
import matplotlib.pyplot as plt
import scipy

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 


vec_h = scipy.vectorize(h, otypes=[float])

N = np.linspace(0, 19, 20)
plt.stem(N, vec_h(N))
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Filter Impulse Response')
plt.savefig('../figs/5.2.png')
plt.show()