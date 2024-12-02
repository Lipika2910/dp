'''
import hashlib

input_string = input("Enter string : ")

sha256_hash = hashlib.sha256()
sha256_hash.update(input_string.encode('utf-8'))
hash_hex = sha256_hash.hexdigest()

print("SHA-256 Hash: ", hash_hex)
'''
import hashlib
lp=input("enter")
hash=hashlib.sha256()
hash.update(lp.encode('utf-8'))
hhash=hash.hexdigest()
print(hhash)
