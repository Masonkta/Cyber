#Mason Maddox
import socket
from sys import stdout
from time import time



ip = "138.47.99.64"
port = 31337
#138.47.165.156 on port 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

binString1 = ''
binString2 = ''
avg = []




def covert(nums):
    
    shift1 = 8
    l1 = []

    for i in range(0, len(nums), shift1):
        binValue = nums[i:i+shift1]
        l1.append(binValue)
    
    
    binaryString_ASCII8(l1)
    
    
def binaryString_ASCII8(bits): #Converts Binary List into String and Returns Output
    
    result = ''
    for i in bits:
        if(len(i) != 8):
            pass
        else:
            if(int(i,2) == 8):
                result = result.rstrip(result[-1])
            else:   
                result = result+chr(int(i,2))
    
    
    
    if(result.find("EOF") != -1):
        result = result[:result.find("EOF")]
        print(result)
        print()

    else:
        print("NO MESSAGE FOUND")
        print()

def average(lst):
    return sum(lst)/len(lst)


data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    
    stdout.write(data)
    stdout.flush()


    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)
    
    avg.append(delta)
   
    

s.close()
print("Connection closed")

check = average(avg)
print(check)

for i in range(len(avg)):
    if (avg[i] >= .08):
        binString1 = binString1+'1'
        binString2 = binString2+'0'
    else:
        binString1 = binString1+'0'
        binString2 = binString2+'1'



print("1-0 Message:")
covert(binString1)
print("0-1 Message:")
covert(binString2)


