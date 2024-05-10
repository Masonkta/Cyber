import sys

# Global variables with default values
patterns_in = ['o', 'l']
patterns_out = ['0', '1']

def main():
    if (sys.argv[1][-4:] != '.txt'):
        print("Usage: python patternDecoder.py [file.txt] [pattern_in_0] [pattern_out_0] ...")
    if len(sys.argv) > 2:
        if (len(sys.argv[2:]) % 2 != 0):
                 print("Usage: Every pattern must include an input and output")

        patterns_in = []
        patterns_out = []
        for i, pattern in enumerate(sys.argv[2:]):
            if i % 2 == 0:
                patterns_in.append(pattern)
            else:
                patterns_out.append(pattern)
    print(patterns_in)
    print(patterns_out)

if __name__ == "__main__":
    main()

