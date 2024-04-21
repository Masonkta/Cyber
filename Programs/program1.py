##############################
# Name: Brady Burns
# Assignment: Program 1 - Intro to Cyber Security
# Date: 3/20/24
##############################


# Imports
import sys

# Functions
def get_bit_length(bin_input):
    for char in bin_input:
        if (ord(char) > 127):
            return 8
    return 7
def bin_to_ascii(bin_input, bit_length):
    if bit_length == 8:
        bytes_list = [bin_input[i:i+8] for i in range(0, len(bin_input), 8)]
    else:
        bytes_list = [bin_input[i:i+7] for i in range(0, len(bin_input), 7)]
    ascii_chars = [chr(int(byte, 2)) for byte in bytes_list]
    ascii_text = ''.join(ascii_chars)

    return ascii_text
# Main
# sys.stdin.read().strip() to get from stdin
bin_input = sys.stdin.read().strip()

ascii_text = bin_to_ascii(bin_input, get_bit_length(bin_input))
print(ascii_text)
