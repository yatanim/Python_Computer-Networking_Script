import socket

s=socket.socket()
print("socket created successfully")

port=1007

s.bind(("",port))
print(f"socket is binded to {port}")

s.listen(5)
print("socket is listening")

while True:
    c,addr=s.accept()
    print(f"got connection from {addr}")
    c.send(b'thank u for your connection')
    c.close()
