import hashlib
import subprocess
import time
import sys

# Connect to the server using netcat
try:
    output = subprocess.check_output(['nc', 'localhost', '54321'], timeout=5)
    current_time_input = output.decode().strip()  # Received current system time from server
except subprocess.CalledProcessError:
    print("Failed to connect to the server.")
    sys.exit(1)
except subprocess.TimeoutExpired:
    print("Connection timed out.")
    sys.exit(1)

# Parse received current system time
try:
    current_time_struct = time.strptime(current_time_input, "%Y-%m-%d %H:%M:%S")
except ValueError:
    print("Invalid time format received from the server.")
    sys.exit(1)

current_time_seconds = time.mktime(current_time_struct)

# Read epoch time
epoch_time_string = "2024 05 08 05 24 00"
epoch_time_struct = time.strptime(epoch_time_string, "%Y %m %d %H %M %S")
epoch_time_seconds = time.mktime(epoch_time_struct)

# Calculate elapsed time and interval
elapsed = current_time_seconds - epoch_time_seconds
offset = int(elapsed) % 60
interval = int(elapsed) - offset

# Calculate hashed result
result = hashlib.md5(str(interval).encode())
result = hashlib.md5(result.hexdigest().encode()).hexdigest()

# Extract first two letters and last two digits
hashed_string = ''.join(c for c in result if c.isalpha())[:2]
hashed_number = ''.join(c for c in result[::-1] if c.isdigit())[:2]

# Print hash code
print("HASH CODE:", hashed_string + hashed_number)

