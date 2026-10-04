import hashlib

target_hash = "your hash here"

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as f:
  for line in f:
    word = line.strip()
    attempt = hashlib.md5(word.encode()).hexdigest()
    if attempt == target_hash:
      print("Password found:", word)
      break
