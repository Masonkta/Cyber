import sys
import hashlib
import time
import pytz

# Read epoch time
epoch_time_string = "2024 05 08 05 24 00"
epoch_time_struct = time.strptime(epoch_time_string, "%Y %m %d %H %M %S")
epoch_time_seconds = time.mktime(epoch_time_struct)

# Determine if testing mode is enabled
testing = False

# Get current system time in UTC
if testing:
    current_time_input = input("Enter current system time (YYYY MM DD HH MM SS): ")
    try:
        current_time_struct = time.strptime(current_time_input, "%Y %m %d %H %M %S")
    except ValueError:
        print("Invalid input format. Please enter the time in the format YYYY MM DD HH MM SS.")
        sys.exit(1)
    current_time_seconds = time.mktime(current_time_struct)
else:
    current_time_seconds = time.time()

sys_time_utc = time.gmtime(current_time_seconds)

# Calculate elapsed time and interval
elapsed = current_time_seconds - epoch_time_seconds
offset = int(elapsed) % 60
interval = int(elapsed) - offset

# Debug prints
print("Epoch Time:", time.strftime("%Y-%m-%d %H:%M:%S", epoch_time_struct))
print("Current System Time (UTC):", time.strftime("%Y-%m-%d %H:%M:%S", sys_time_utc))
print("Elapsed Time (seconds):", elapsed)
print("Offset (seconds):", offset)
print("Interval (seconds):", interval)

# Calculate hashed result
result = hashlib.md5(str(interval).encode())
result = hashlib.md5(result.hexdigest().encode()).hexdigest()

# Extract first two letters and last two digits
hashed_string = ''.join(c for c in result if c.isalpha())[:2]
hashed_number = ''.join(c for c in result[::-1] if c.isdigit())[:2]

# Print hash code
print("HASH CODE:", hashed_string + hashed_number)
