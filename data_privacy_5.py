'''
import random

def generate_password(length, file_path):
    

    with open(file_path, 'r') as file:
        all_characters = file.read()
    
    
    lowercase_letters = [char for char in all_characters if char.islower()]
    uppercase_letters = [char for char in all_characters if char.isupper()]
    numbers = [char for char in all_characters if char.isdigit()]
    special_characters = [char for char in all_characters if not char.isalnum()]

   
    password = [
        random.choice(uppercase_letters),
        random.choice(numbers),
        random.choice(special_characters),
    ]
    
   
    while len(password) < length:
        password.append(random.choice(lowercase_letters))
    
    random.shuffle(password)
    
    
    return ''.join(password)


file_path = 'password_characters.txt'  
password_length = int(input("enter length of passwords : "))
generated_password = generate_password(password_length, file_path)
print(f"Generated password: {generated_password}")


'''


import random

iny=int(input("en"))
with open('password_characters.txt','r') as file:
  line=file.read()




uppercase=[char for char in line if char.isupper()]
lowercase=[char for char in line if char.islower()]
digit=[char for char in line if char.isdigit()]
special=[char for char in line if char.isalnum()]


password=[
    random.choice(uppercase),
     random.choice(special),
    random.choice(digit)
]



if len(password)<iny:
  password.append(random.choice(lowercase))


random.shuffle(password)

print(''.join(password))
