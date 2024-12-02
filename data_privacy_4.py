import hashlib
import requests

def get_sha1_hash(password):
   
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

def check_pwned_password(password):
    
    
    sha1_password = get_sha1_hash(password)
    

    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
  
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data: {response.status_code}")
    
   
    hashes = (line.split(':') for line in response.text.splitlines())
    
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return f"Password found {count} times in breaches!"
    
    return f"Password not found in any breaches."




with open('passwords.txt', 'r') as f:
    Lines = f.readlines() 

print(Lines)

print("\n\nData Breach info : \n")


for lines in Lines:
  l=lines.split(',')
  m=l[1].strip()
  password_to_check =m
  print("password is : ",m)
  result = check_pwned_password(password_to_check)
  print(result)
  print("-----------------------------------")


