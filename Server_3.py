#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
    print(s.recv(1024).decode())
    s.send("acknowledgement recived from the server".encode())



# In[ ]:




