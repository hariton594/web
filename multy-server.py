import socket                                                                  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                            
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 2222))                                                              
s.listen(10)                                                                    
print('start listening')
while True:
	conn, addr = s.accept()
	print('new connection', addr)                                                        
	while True:                                                                    
                data = conn.recv(1024)                                          
                if data=='close' :
			print('get close')                                         
                	conn.send(data)                                                
	conn.close()
