import sys

def store(offset, interval):
    
    save = offset

    try:
        wrapper = open(w, 'rb')
    except FileNotFoundError:
        print("Wrapper File Name Doesnt Exist")
        return

    try:
        hidden = open(h, 'rb')
    except FileNotFoundError:
        print("Wrapper File Name Doesnt Exist")
        return
        
    wrapper = bytearray(wrapper.read())
    hidden = bytearray(hidden.read())

    if(bitByte == '-B'):

        i = 0
    
        while(i < len(hidden)):
            if(offset >= len(wrapper)):
                wrapper.append(0x00)
            else:
                wrapper[offset] = hidden[i]
                offset += interval
                i+=1

        i = 0

        while(i < len(sentinel)):
            if(offset >= len(wrapper)):
                wrapper.append(0x00)
            else:
                wrapper[offset] = sentinel[i]
                offset += interval
                i+=1
  

    
    if(bitByte == '-b'):
        i=0
        while(i < len(hidden)):
            for j in range(7):
                wrapper[offset] &= 0b11111110
                wrapper[offset] |= ((hidden[i]& 0b10000000) >> 7)
                if(hidden[i] << 1 > 255):
                    hidden[i] = (hidden[i]<<1)&(2**8-1)
                else:
                    hidden[i]<<=1
                
                offset += interval
            i+=1
        i=0
        while(i < len(sentinel)):
            for j in range(7):
                wrapper[offset] &= 0b11111110
                wrapper[offset] |= ((sentinel[i] & 0b10000000) >> 7)
                if(sentinel[i] << 1 > 255):
                    sentinel[i] = (sentinel[i]<<1)&(2**8-1)
                else:
                    sentinel[i] <<=1
                offset += interval
            i+=1

    sys.stdout.buffer.write(wrapper)    

        

def retrieve(offset, interval):
    try:
        wrapper = open(w, 'rb')
    except FileNotFoundError:
        print("Wrapper File Name Doesnt Exist")
        return
    
    wrapper = bytearray(wrapper.read())
    h = []
    checkSent = []
    check = 0

    if(bitByte == '-B'):
        
        while(offset < len(wrapper)):

            b = wrapper[offset]
            if(b == sentinel[0]):
                checkSent = []
                offset2 = offset
                test = b
                for byte in sentinel:
                    checkSent.append(test)
                    offset2+=interval
                    if(offset2 > len(wrapper)):
                        pass
                    else:
                        test = wrapper[offset2]
                if(checkSent == sentinel):
                    offset=offset2+interval
                    b = wrapper[offset]
                    break
                        #print("FOUND")
                    
                
            h.append(b)            
            offset += interval

        sys.stdout.buffer.write(bytearray(h))
    
    if(bitByte == '-b'):
        wrapper = open(w, 'rb')
        hidden = []
        hidden_sentinel = []
        sentinel_count = 0
        wrapper_byte_array = bytearray(wrapper.read())
    
        while(offset < len(wrapper_byte_array)):
            # current bit
            wrapper_byte = wrapper_byte_array[offset]
            lsb_shift = 0
            
            # lsb: least significant bit of current byte
            for j in range(8):
                if offset >= len(wrapper_byte_array):
                    break
                
                # grab lsb
                lsb = wrapper_byte_array[offset] & 1
                lsb_shift = lsb_shift ^ (lsb << 7-j) # 7-j # this might have to be reversed?

                # increment offset
                offset += interval

            byte = lsb_shift#bytearray(lsb_shift)
            
            # check if byte matches sentinel
            if byte == sentinel[sentinel_count]:
                # save byte, update sentinel index
                hidden_sentinel.append(byte)
                sentinel_count += 1
            else:
                # if hidden sentinel is full, then store values and reset
                if len(hidden_sentinel) > 0:
                    #print(len(hidden_sentinel))
                    hidden_sentinel.reverse()
                    for byte_hs in hidden_sentinel:
                        hidden.append(byte_hs)
                    sentinel_count = 0
                    hidden_sentinel = []

                # save current byte to final file
                hidden.append(byte)

            # check sentinels
            if hidden_sentinel == sentinel:
                break

        # output
        sys.stdout.buffer.write(bytearray(hidden))
        wrapper.close()

#===MAIN===#

sentinel = [0x0,0xff,0x0,0x0,0xff,0x0]

mode = ''

bitByte = ''

o = 0

inter = 1

w = ''

h = ''

#TAKE IN PARAMETERS
mode = sys.argv[1]

bitByte = sys.argv[2]

#checks for offset, interval, hidden, and wrapper then strips and stores them into variables
for check in sys.argv:
    if('-o' in check):
        o = int(check.replace('-o',''))
        #print(o)
    if('-i' in check):
        inter = int(check.replace('-i',''))
        #print(inter)
    if('-w' in check):
        w = str(check.replace('-w',''))
        #print(w)
    if('-h' in check):
        h = str(check.replace('-h',''))
        #print(h)

#CHECK MODE
if(mode == '-s'):
    store(o,inter)

if(mode == '-r'):
    retrieve(o,inter)
