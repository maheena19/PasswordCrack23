# PasswordProject 
- 2nd 9Weeks Major Project: Cybersecurity
- Maheen Ali 

# Dependencies 
- You need to upload top 10k passwords because the dictionary method depends on it to work
- You need to add apostrophes next too Bcrypt Hash or the method to work 

# Command Line Arguments 

Hash types:

-md5 : MD5

-s256 : SHA-256

-bc : BCrypt

-pt : PlainText

Methods:

-B : Brute Force 

-D : Dictionary

# Formatting 
- python3 pwcrack.py qwerty -pt -B
- python3 pwcrack.py 5d41402abc4b2a76b9719d911017c592 -md5 -D
- python3 pwcrack.py '$2y$10$i2Rbs2hRTCf46BwgfD9vg.NZY9JHCDAYhmi6yPKyv4LiG9HzxlPVm' -D -bc
- python3 pwcrack.py maheen -pt -D   
- python3 pwcrack.py 12345678
- python3 pwcrack.py 'a9c43be948c5cabd56ef2bacffb77cdaa5eec49dd5eb0cc4129cf3eda5f0e74c' -s256 -D


