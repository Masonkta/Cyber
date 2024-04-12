def convertTextToBin():
	# put zeroone string from initial file into string
    string = ""
    bin_string = ""
    ascii_chars = ""
    substring = ""
    while len(string) > 0:
        if (string[0:4] == "zero"):
            bin_string += "0"
            string = string[4:]
        elif (string[0:3] == "one"):
            bin_string += "1"
            string = string[3:]
    if len(bin_string) % 7 == 0:
        for i in range(0, len(bin_string), 7):
            substring = bin_string[i:i + 7]
            ascii_value = int(substring, 2)
            ascii_chars += chr(ascii_value)
    elif len(bin_string) % 8 == 0:
        for i in range(0, len(bin_string), 8):
            substring = bin_string[i:i + 8]
            ascii_value = int(substring, 2)  # Corrected from '8' to '2'
            ascii_chars += chr(ascii_value)
    print(ascii_chars)

convertTextToBin()

