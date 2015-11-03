import time
import socket

print("Hello world!")
time.sleep(2)


print("#Hello world!")
time.sleep(1)
print("Hello #world!")
time.sleep(2)
print("#Hello #world!")
time.sleep(2)
print("Hello world!")
time.sleep(1)
print("Hello world!")
time.sleep(1)
print("Hello world!")
time.sleep(1)
print("\Hello \world!")
time.sleep(1)
print("#Hello #world!")
time.sleep(3)
print("Please enter your IP and port like this: IP:port, ex: 128.478.1.4:28463; as #input")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('#input', port))
s.send("[Console] Hello!")
data = s.recv(1024)
s.close
print("[#input] ", data)