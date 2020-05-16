import socket

data1 = "send"
s = socket.socket()
port = 8080
s.bind(('', port))
s.listen(5)
while True:
    conn, addr = s.accept()
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        else:         
            print ("Received Message", (data))
c.close()
