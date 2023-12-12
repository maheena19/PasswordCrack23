import sys
import hashlib
#import bcrypt

# Global variables to store hash type, crack method, and dictionary file
hash_type = ""
crack_method = ""
dictionary_file = ""


# Function to set the hash type
def set_hash_type(ht):
    global hash_type
    hash_type = ht

def set_cracking_method(cm):
    global cracking_method, dictionary_file
    cracking_method = cm
    if cm == "Dictionary":
        dictionary_file = ""

def is_hash_type(ht_check):
    return ht_check == hash_type

# Check if a password was given. If not, exit the program.
# Options are -p Plain text, -m MD5, -b BCrypt, -s SHA256, -D Dictionary, -B Brute force
given_password = sys.argv[1]
if given_password in ['-p', '-m', '-b', '-s', '-D', '-B']:
    print("**No password given to crack.**")
    quit()

# Process arguments after the password and set hash type and cracking method
given_arguments = sys.argv[2:]

for arg in given_arguments:
    if arg == "-p":
        set_hash_type("PlainText")
    elif arg == "-m":
        set_hash_type("MD5")
    elif arg == "-b":
        set_hash_type("BCrypt")
    elif arg == "-s":
        set_hash_type("SHA-256")
    elif arg == "-D":
        set_cracking_method("Dictionary")
    elif arg == "-B":
        set_cracking_method("Brute Force")

# Assign defaults if not given
if len(hash_type) == 0:
    print("**No hash type given. Defaulting to PlainText**")
    set_hash_type("PlainText")
if len(cracking_method) == 0:
    print("**No cracking method selected. Defaulting to Dictionary.**")
    set_cracking_method("Dictionary")
if cracking_method == "Brute Force" and not (hash_type == "PlainText"):
    print("**Invalid combination. Brute Force is only compatible with PlainText**")
    quit()

# Search the dictionary for the password based on the hash type
if cracking_method == "Dictionary":
    dictionary = open("Top10kPasswords.txt")
    print("Searching the Dictionary...")
    for line in dictionary:
        temp_line = line.rstrip().encode('utf-8')
        if is_hash_type("MD5"):
            hashed_temp_line = hashlib.md5(temp_line)
            check = hashed_temp_line.hexdigest()
        elif is_hash_type("SHA-256"):
            hashed_temp_line = hashlib.sha256(temp_line)
            check = hashed_temp_line.hexdigest()
        elif is_hash_type("PlainText"):
            check = line.rstrip()
        elif is_hash_type("BCrypt"):
            temp_hash = given_password.rstrip().encode('utf-8')
            check = ""
            if bcrypt.checkpw(temp_line, temp_hash):
                print("Password Found: " + line)
                quit()

        if check == given_password and not is_hash_type("BCrypt"):
            print("Password Found: " + line)
            quit()
    print("Password not found in dictionary.")
    quit()

# Brute force a PlainText password with characters [a-z], [A-Z], and [0-9]
if cracking_method == "Brute Force":
    print("Brute Forcing...")
    temp_pass = ""
    pass_without_whitespace = given_password.rstrip()
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

# Function to set the crack method
def set_crack_method(cm):
    global crack_method, dictionary_file
    crack_method = cm
    if cm == "Dictionary":
        dictionary_file = ""

