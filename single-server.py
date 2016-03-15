import socket                                                                  
s = socket.socket()                                                            
s.bind(('', 2222))                                                              
s.listen(1)                                                                    
conn, addr = s.accept()                                                        
while True:                                                                    
                data = conn.recv(1024)                                          
                if data=='close' : break                                        
                conn.send(data)                                                
conn.close()
