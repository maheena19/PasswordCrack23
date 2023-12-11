import sys
import hashlib
import bcrypt

# Global variables to store hash type, crack method, and dictionary file
hash_type = ""
crack_method = ""
dictionary_file = ""


# Function to set the hash type
def set_hash_type(ht):
    global hash_type
    hash_type = ht


# Function to set the crack method
def set_crack_method(cm):
    global crack_method, dictionary_file
    crack_method = cm
    if cm == "Dictionary":
        dictionary_file = ""

