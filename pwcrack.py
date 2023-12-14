import sys
import hashlib
import bcrypt

# Type is the kind of hash and method is either Brute Force or Dictionary
# Dictionary_file is for the dictionary.
# Global variables to store hash type, crack method, and dictionary file
hash_type = ""
method = ""
dictionary_file = ""
typeList = ["md5", "plaintext", "bcrypt", "sha-256"]

# Function to set the hash type

def check_hash_type(c):
    if c == hash_type:
        return True
    return False

def set_hash_type(t):
    global hash_type
    hash_type = t

def set_method(m):
    global method, dictionary_file
    method = m
    if m == "Dictionary":
        dictionary_file = ""


# if password is not given it will set to a default 
# options are -pt Plain text, -md5 MD5, -bC BCrypt, -s256 SHA256, -D Dictionary, -B Brute force
password = sys.argv[1]
if password in ['-p', '-m', '-b', '-s', '-D', '-B']:
    print("Password is not given to crack.")
    quit()

# Runs through arguments after password and sets a type and method
given_arguments = sys.argv[2:]

for arg in given_arguments:
    if arg == "-pt":
        set_hash_type("PlainText")
    elif arg == "-md5":
        set_hash_type("MD5")
    elif arg == "-bc":
        set_hash_type("BCrypt")
    elif arg == "-s256":
        set_hash_type("SHA-256")
    elif arg == "-D":
        set_method("Dictionary")
    elif arg == "-B":
        set_method("Brute Force")

# Assigns type and method if not given. Because Brute Force only works with PlainText
# in this program, checks to see if the user has inputted anything else with Brute Force.
if len(hash_type) == 0:
    print("You need to enter a type given if not given it will default to PlainText")
    set_hash_type("PlainText")
if len(method) == 0:
    print("No method selected is selected so it will default to Dictionary.")
    set_method("Dictionary")
if method == "Brute Force" and not (hash_type == "PlainText"):
    print("This is not a possible combination because brute Force is only compatible with PLainText")
    quit()

# Runs through each line in the dictionary (top 10k passwords) and checks the appropriate
# type of hash. Returns the PlainText  line if found.
if method == "Dictionary":
    d = open("Top10kPasswords.txt")
    print("Searching the Dictionary...")
    for line in d:
        temp_line = line.rstrip().encode('utf-8')
        if check_hash_type("MD5"):
            hashed_temp_line = hashlib.md5(temp_line)
            check = hashed_temp_line.hexdigest()
        elif check_hash_type("SHA-256"):
            hashed_temp_line = hashlib.sha256(temp_line)
            check = hashed_temp_line.hexdigest()
        elif check_hash_type("PlainText"):
            check = line.rstrip()
        elif check_hash_type("BCrypt"):
            temp_hash = password.rstrip().encode('utf-8')
            check = ""
            if bcrypt.checkpw(temp_line, temp_hash):
                print("Password Found: " + line)
                quit()


        if check == password and not check_hash_type("BCrypt"):
            print("Password Found: " + line)
            quit()
    print("Password is not found in the dictionary.")
    quit()

# Brute forces a PlainText password with characters [a-z], [A-Z], and [0-9]
if method == "Brute Force":
    print("Brute Forcing...")
    temp_pass = ""
    pass_without_whitespace = password.rstrip()
    possible_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for x in pass_without_whitespace:
        for val in possible_values:
            if x == val:
                temp_pass += val
                if temp_pass == pass_without_whitespace:
                    print("Password Found: " + temp_pass)
                    quit()
    print("Unable to Find Password")
    quit()
