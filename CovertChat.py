import socket
from sys import stdout
from time import *

port = 31337
ip = '138.47.99.64'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))
binary = ""
values = []

# receive data until EOF
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	values.append(delta)
	if(delta >= 0.09):
		binary += "1"
	else:
		binary += "0" 




# close the connection to the server
s.close()
#print(binary)
print(values)

byte_size = 8
binary_bytes = [binary[i:i+byte_size] for i in range(0, len(binary), byte_size)]
print(binary_bytes)

ascii_string = ''.join([chr(int(byte, 2)) for byte in binary_bytes])
final = ""
final = ascii_string.split("EOF", 1)[0]
print("ASCII representation:", final)