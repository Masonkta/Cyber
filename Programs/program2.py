##############################
# Name: Brady Burns
# Assignment: Program 2 - Intro to Cyber Security
# Date: 3/20/24
##############################


# Imports
import sys

# Functions
def vigenere_cipher(input_text, key, mode):
    key = ''.join(filter(str.isalpha, key.upper()))

    result = ""
    key_i = 0

    for char in input_text:
        # Convert if alpha-numeric, otherwise append
        if char.isalpha():
            # shift = ASCII(key_i % len(key)) - shift(a)
            shift = ord(key[key_i % len(key)]) - ord('A')
            if mode == '-d':
                shift = -shift
            
            # result = (ASCII - ASCII(a) + shift) % 26) + ASCII(a)
            if char.islower():
                result += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            
            key_i += 1
        else:
            result += char
    return result

# Main
if len(sys.argv) != 3 or sys.argv[1] not in ['-e', '-d']:
    print("Usage: <python_ver> < <-e/-d> <key>")
    sys.exit(1)
    
mode = sys.argv[1]
key = sys.argv[2]

#try:
while True:
    try:
        input_text = input().strip()
        result = vigenere_cipher(input_text, key, mode)
        print(result)
    except EOFError:
        break
    except KeyboardInterrupt:
        print()
        sys.exit(1)
        
#except KeyboardInterrupt:
#    print()
#    sys.exit(1)

