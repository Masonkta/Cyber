import sys

def xor_bytes(phrase, key):
    # Repeat the key cyclically until it matches the size of the message
    repeated_key = key * (len(phrase) // len(key)) + key[:len(phrase) % len(key)]
    
    #reads the key data as bytes, saves data in result 
    result = bytearray(len(phrase))
    for i in range(len(phrase)):
        result[i] = phrase[i] ^ repeated_key[i]
    return result 

def main():
    #opens key files
    with open("key", "rb") as file:
        key = file.read()
    phrase = sys.stdin.buffer.read()
    #XOR encrypt/decrypt
    result = xor_bytes(phrase, key)
    sys.stdout.buffer.write(result)

if __name__ == "__main__":
    main()
