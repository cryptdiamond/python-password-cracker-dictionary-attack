import hashlib
 
word = "hello123"          # change this to whatever word you want to hash
algorithm = "md5"          # options: md5, sha1, sha256, sha512
 
h = hashlib.new(algorithm)
h.update(word.encode())
print(f"{algorithm.upper()} hash of '{word}': {h.hexdigest()}")
