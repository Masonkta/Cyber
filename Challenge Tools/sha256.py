import hashlib

# Function to combine two passwords and hash the combination using SHA256
def combine_and_hash(password1, password2):
    combined1 = password1 + password2
    combined2 = password2 + password1

    hash1 = hashlib.sha256(combined1.encode()).hexdigest()
    hash2 = hashlib.sha256(combined2.encode()).hexdigest()

    return hash1, hash2

# Given SHA256 hash value
given_hash = "d05e23dccaaadda9f7e8785791aacc1763a3770531e27910eafc4573943c4dbd"

# List of passwords to test
passwords = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666",
    "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "pussy", "superman", "1qaz2wsx", "7777777",
    "fuckyou", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm",
    "asdfgh", "hunter", "buster", "soccer", "harley",
    "batman", "andrew", "tigger", "sunshine", "iloveyou",
    "fuckme", "2000", "charlie", "robert", "thomas",
    "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "asshole", "computer", "michelle",
    "jessica", "pepper", "1111", "zxcvbn", "555555",
    "11111111", "131313", "freedom", "777777", "pass",
    "fuck", "maggie", "159753", "aaaaaa", "ginger",
    "princess", "joshua", "cheese", "amanda", "summer",
    "love", "ashley", "6969", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix",
    "minecraft"
]

# Iterate through all combinations of passwords
for i in range(len(passwords)):
    for j in range(i+1, len(passwords)):
        password1 = passwords[i]
        password2 = passwords[j]

        hash1, hash2 = combine_and_hash(password1, password2)

        if hash1 == given_hash:
            print(f"Password combination found: {password1} + {password2}")
        elif hash2 == given_hash:
            print(f"Password combination found: {password2} + {password1}")
