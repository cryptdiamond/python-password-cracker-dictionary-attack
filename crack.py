import hashlib
 
target_hash = "your hash here"
algorithm = "md5"   # change to sha1, sha256, sha512, etc. if md5 doesn't work
wordlist_path = "/usr/share/wordlists/rockyou.txt"
 
target_hash = target_hash.lower().strip()
 
with open(wordlist_path, "r", encoding="latin-1") as f:
    for i, line in enumerate(f):
        word = line.strip()
        h = hashlib.new(algorithm)
        h.update(word.encode())
        attempt = h.hexdigest()
 
        if attempt == target_hash:
            print(f"Password found: {word}")
            break
 
        if i % 500000 == 0 and i != 0:
            print(f"Checked {i} words so far...")
    else:
        print("Password not found in wordlist with this algorithm.")
        print("Try a different algorithm, or the password may not be in this wordlist.")
