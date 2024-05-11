import sys
import argparse

SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

def store_byte_mode(offset, interval, wrapper_file, hidden_file):
    """Store hidden data using byte mode."""
    with open(wrapper_file, 'rb') as wrapper:
        wrapper_data = bytearray(wrapper.read())

    with open(hidden_file, 'rb') as hidden:
        hidden_data = bytearray(hidden.read())

    i = 0
    while i < len(hidden_data):
        if (offset >= len(wrapper_data)):
            wrapper_data.append(0x00)
        else:
            wrapper_data[offset] = hidden_data[i]
            i += 1
    
    i = 0
    while i < len(SENTINEL):
        if offset >= len(wrapper_data):
            wrapper.append(0x00)
        else:
            wrapper_data[offset] = SENTINEL[i]
            offset += interval
            i += 1
    
    sys.stdout.buffer.write(wrapper_data)

def store_bit_mode(offset, interval, wrapper_file, hidden_file):
    pass

def retrieve_byte_mode(offset, interval, wrapper_file):
    """Retrieve hidden data using byte mode."""
    with open(wrapper_file, 'rb') as wrapper:
        wrapper_data = bytearray(wrapper.read())
    
    extracted_data = bytearray()
    checkSent = []
    check = 0

    while offset < len(wrapper_data):
        b = wrapper_data[offset]
        if b == SENTINEL[0]:
            checkSent = []
            offset2 = offset
            test = b
            for byte in SENTINEL:
                checkSent.append(test)
                offset2 += interval
                if offset2 <= len(wrapper_data):
                    test = wrapper_data[offset2]
            if checkSent == SENTINEL:
                offset = offset + interval
                b = wrapper_data[offset]
                break
        extracted_data.append(b)
        offset += interval
    
    sys.stdout.buffer.write(extracted_data)

def retrieve_bit_mode(offset, interval, wrapper_file):
    with open(wrapper_file, 'rb') as wrapper:
        wrapper_data = bytearray(wrapper.read())

    hidden = []
    hidden_sentinel = []
    sentinel_count = 0

    while(offset < len(wrapper_data)):
        wrapper_byte = wrapper_data[offset]
        lsb_shift = 0

        # lsb: least significant bit of current byte
        for j in range(8):
            if offset >= len(wrapper_data):
                break

            # grab lsb
            lsb = wrapper_data[offset] & 1
            lsb_shift = lsb_shift ^ (lsb << 7-j)

            offset += interval

        byte = lsb_shift#bytearray(lsb_shift)

        # check if byte matches sentinel
        if byte == SENTINEL[sentinel_count]:
            # save byte, update sentinel index
            hidden_sentinel.append(byte)
            sentinel_count += 1
        else:
            # if hidden sentinel is full, then store values and reset
            if len(hidden_sentinel) > 0:
                hidden_sentinel.reverse()
                for byte_hs in hidden_sentinel:
                    hidden.append(byte_hs)
                sentinel_count = 0
                hidden_sentinel = []

                # save current byte to final file
            hidden.append(byte)

        if hidden_sentinel == SENTINEL:
            break
    sys.stdout.buffer.write(bytearray(hidden))

def main():
    """Main function to parse command-line arguments and execute appropriate operations."""
    # Initialize argument parser with description
    parser = argparse.ArgumentParser(description="Hide or retrieve data from a wrapper file using steganography")

    # Define command-line arguments
    parser.add_argument("-s", action="store_true", help="Store hidden data")
    parser.add_argument("-r", action="store_true", help="Retrieve hidden data")
    parser.add_argument("-b", action="store_true", help="Bit mode")
    parser.add_argument("-B", action="store_true", help="Byte mode")
    parser.add_argument("-o", type=int, default=0, help="Offset value (default is 0)")
    parser.add_argument("-i", type=int, default=1, help="Interval value (default is 1)")
    parser.add_argument("-w", type=str, required=True, help="Wrapper file path")
    parser.add_argument("-f", type=str, help="Hidden file path")

    # Parse command-line arguments
    args = parser.parse_args()
    
    # Check for conflicting options
    if args.s and args.r:
        print("Error: Both store (-s) and retrieve (-r) options cannot be specified at the same time.")
        sys.exit(1)

    if args.B and args.b:
        print("Error: Both byte mode (-B) and bit mode (-b) cannot be specified at the same time.")
        sys.exit(1)

    # Perform the specified operation
    if args.s:  # Store hidden data
        if args.B:  # Byte mode
            store_byte_mode(args.o, args.i, args.w, args.f)
        elif args.b:  # Bit mode
            store_bit_mode(args.o, args.i, args.w, args.f)
        else:
            print("Error: Either byte mode (-B) or bit mode (-b) must be specified.")
            sys.exit(1)
    elif args.r:  # Retrieve hidden data
        if args.B:  # Byte mode
            retrieve_byte_mode(args.o, args.i, args.w)
        elif args.b:  # Bit mode
            retrieve_bit_mode(args.o, args.i, args.w)
        else:
            print("Error: Either byte mode (-B) or bit mode (-b) must be specified.")
            sys.exit(1)
    else:
        print("Error: Either store (-s) or retrieve (-r) option must be specified.")
        sys.exit(1)

if __name__ == "__main__":
    main()

