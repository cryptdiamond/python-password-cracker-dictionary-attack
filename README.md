# Python Password Cracker Using Dictionary Attack

A Python tool that demonstrates how dictionary attacks work against hashed passwords. Supports multiple hash algorithms (MD5, SHA-1, SHA-256, SHA-512) and uses the rockyou.txt wordlist to systematically hash common passwords and compare them against a target hash until a match is found.

## Files

* `create_hash.py` - Generates a hashed password to crack, using a configurable algorithm
* `crack.py` - Cracks the hash using a dictionary attack, with progress updates as it works through the wordlist

## Tools Used

Python, hashlib (MD5 / SHA-1 / SHA-256 / SHA-512), Dictionary Attack, Kali Linux, rockyou.txt

## How It Works

1. Run `create_hash.py` to generate a target hash (set the `word` and `algorithm` variables inside the script)
2. Copy the hash into `crack.py`'s `target_hash` variable
3. Make sure `crack.py`'s `algorithm` variable matches the algorithm used to create the hash
4. Run `crack.py` to find the original password. It checks each word in rockyou.txt, printing progress every 500,000 words, and reports if the password isn't found in the wordlist

## Requirements

* Python 3
* rockyou.txt wordlist (included with Kali Linux at `/usr/share/wordlists/rockyou.txt`, may need to be decompressed first with `sudo gunzip /usr/share/wordlists/rockyou.txt.gz`)

## Notes

This is an educational tool for understanding how dictionary attacks work, not a general-purpose password cracker. It can only find passwords that exist in the wordlist used, and only if the correct hash algorithm is selected. For real-world password auditing, tools like `hashcat` or `john` are far faster since they're optimized and can use GPU acceleration.
