# Program:  Byte Method Steganography
# Desc:     Given an image to hide, this program will embed a JPEG image in another JPEG image using the byte method. 


# --- USAGE --- 
""" 
Command Line:
python3 steg.py -o [OFFSET] -i [INTERVAL] -w [WRAPPER FILE] -H [FILE TO HIDE] --output [FILE TO OUTPUT RESULT]

Note: Be sure to check that -H file is small enough to be embedded in -w file.
"""


# --- LIBRARIES ---
import sys
import argparse


# --- CONSTANTS ---
STORE = None 
RETRIEVE = None
WRAPPER = None
HIDDEN = None
OFFSET = None 
INTERVAL = None
OUTPUT = None
sentinel = bytes([0x00, 0xFF, 0x00, 0x00, 0xFF, 0x00])


# --- DEBUG ---
DEBUG = False


# --- METHODS ---
def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--store', required=False, action='store_true', help="Embeds a hidden JPEG within a wrapper JPEG")
    parser.add_argument('-r', '--retrieve', required=False, action='store_true', help="Pulls a hidden JPEG out of a wrapper JPEG")
    parser.add_argument('-o', '--offset', required=True, type=int, help="Offsets <val> number of bytes before encrypting/decrypting")
    parser.add_argument('-i', '--interval', required=True, type=int, help="Embeds a byte of data at <val> interval")
    parser.add_argument('-w', '--wrapper', required=True, help="The wrapper file used to hide the JPEG")
    parser.add_argument('-H', '--hidden', required=False, help="The file to be hidden in the wrapper")
    parser.add_argument('--output', type=str, required=True, help='Output image file')

    args = parser.parse_args()

    global WRAPPER 
    WRAPPER = args.wrapper
    if args.hidden is not None:
        global HIDDEN 
        HIDDEN = args.hidden 
    global OFFSET 
    OFFSET = args.offset 
    global INTERVAL 
    INTERVAL = args.interval 
    global STORE 
    STORE = args.store
    global RETRIEVE 
    RETRIEVE = args.retrieve
    global OUTPUT 
    OUTPUT = args.output

def insertSentinel():
    with open(HIDDEN, "ab") as appendSent:
    appendSent.write(SENTINEL)

def embeddingData():
    with open(HIDDEN, 'rb') as hiddenFile:
        hiddenData = hiddenFile.read() 

    with open(WRAPPER, 'r+b') as wrapperFile:
        wrapperData = bytearray(wrapperFile.read())

    index = OFFSET

    for byte in hiddenData:
        wrapperData[index] = byte
        index += INTERVAL
    
    with open(OUTPUT, 'wb') as outputFile:
        outputFile.write(wrapperData)

def dataExtraction():
    with open(WRAPPER, 'rb') as wrapperFile:
        wrapperData = wrapperFile.read()
    index = OFFSET

    while index < len(wrapperData):
        byte = wrapperData[index]
        if not byte:
            if DEBUG:
                print("End of file reached.")
            break 
        extracted.append(byte)

        if len(extracted) >= 6 and extracted[-6:] == sentinel:
            if DEBUG:
                print("Successfully extracted message")
            break

        index += INTERVAL

    with open(OUTPUT, 'wb') as outputFile:
        outputFile.write(extracted)


# --- DRIVER ---
if __name__ == "__main__":
    parseArgs()

    if STORE is not None:
        insertSentinel()
        embeddingData() 
    
    if RETRIEVE is not None:
        dataExtraction()


# --- PERSONAL DOCUMENTATION ---
# Storage:
# 1.    parse all the command line arguments for use within the program
# 2.    append a sentinel value to the end of the hidden file 
# 3.    embed the data 
#           - first need to open the hidden file and read all the data to memory 
#           - next, open the wrapper file in read write mode 
#           - seek to offset in wrapper file, then write a byte from hidden file to wrapper file at that location 
#           - go to next interval, and add the next byte from hidden file to wrapper 
#           - repeat 
#           - Notes:    Because opening both files in binary mode, seeking will immediately traverse by bytes, not bits.
#                       Also, when using "with open", it automatically closes the files after the method ends. Lastly, the
#                       "bytes" method is a built in method that converts the arguments given into a "byte object". 
#                       Parameter options include decimal numbers, hex values, binary values, etc. 

# Extraction:
# 1.    parse all command line arguments 
# 2.    extract the data 
#           - open wrapper file in read write binary mode 
#           - seek to offset, copy data at that location and append to a byte array 
#           - continuously seek to intervals, copying and appending data until end of file (wrapper)  
