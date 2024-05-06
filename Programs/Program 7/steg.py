import sys
import argparse

SENTINEL = bytearray([0x0, 0xff, 0x0, 0x0, 0xff, 0x0])

def store_byte_mode(offset, interval, wrapper_file, hidden_file):
    """Store hidden data using byte mode."""
    with open(wrapper_file, 'rb') as wrapper:
        wrapper_data = bytearray(wrapper.read())

    with open(hidden_file, 'rb') as hidden:
        hidden_data = bytearray(hidden.read())
    
    wrapper_size = len(wrapper_data)
    hidden_size = len(hidden_data)
    interval = max(interval, 1)

    i = 0
    while i < len(hidden_data):
        wrapper_data[offset] = hidden_data[i]
        offset += interval
        i += 1
    
    i = 0
    while i < len(SENTINEL):
        wrapper_data[offset] = SENTINEL[i]
        offset += interval
        i += 1
    
    with open('output.jpg', 'wb') as output_file:
        output_file.write(wrapper_data)


def retrieve_byte_mode(offset, interval, wrapper_file):
    """Retrieve hidden data using byte mode."""
    with open(wrapper_file, 'rb') as wrapper:
        wrapper_data = bytearray(wrapper.read())
    
    extracted_data = bytearray()
    wrapper_size = len(wrapper_data)
    interval = max(interval, 1)
    offset += len(SENTINEL)  # Skip past the sentinel

    while offset < wrapper_size:
        extracted_data.append(wrapper_data[offset])
        offset += interval
    
    with open('extracted_hidden_data.jpg', 'wb') as extracted_file:
        extracted_file.write(extracted_data)

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
            pass
        else:
            print("Error: Either byte mode (-B) or bit mode (-b) must be specified.")
            sys.exit(1)
    elif args.r:  # Retrieve hidden data
        if args.B:  # Byte mode
            retrieve_byte_mode(args.o, args.i, args.w)
        elif args.b:  # Bit mode
            pass
        else:
            print("Error: Either byte mode (-B) or bit mode (-b) must be specified.")
            sys.exit(1)
    else:
        print("Error: Either store (-s) or retrieve (-r) option must be specified.")
        sys.exit(1)

if __name__ == "__main__":
    main()

