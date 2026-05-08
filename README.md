# Python Password Cracker Using Dictionary Attack

A Python tool that demonstrates how dictionary attacks work
against hashed passwords. Uses MD5 hashing and the rockyou.txt
wordlist to systematically hash common passwords and compare
them against a target hash until a match is found.

## Files
- create_hash.py - Generates a hashed password to crack
- crack.py - Cracks the hash using dictionary attack

## Tools Used
Python, MD5 Hashing, Dictionary Attack, Kali Linux, rockyou.txt

## How It Works
1. Run create_hash.py to generate a target hash
2. Copy the hash into crack.py
3. Run crack.py to find the original password
