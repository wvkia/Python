import socket

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',80))
#发送数据
s.send(b'GET / HTTP/1.1\r')
#接收数据
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
#关闭连接
s.close()

#接收的数据包括HTTP头和网页本身，需要分开，通过\r\n\n
header,html=data.split(b'\r\n\n',1)
print(header.decode('utf-8'))
