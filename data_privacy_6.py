'''
import string 
import itertools
import time

def password_hint(target_password, max_length):

  character=string.ascii_lowercase + string.ascii_uppercase + string.digits

  for i in itertools.product(character,repeat=max_length):
    guess="".join(i)
    print("password guessed : ",guess)
 

    if (guess==target_password):
      print("guess corrected",guess)
      break

  return guess

target_password=input("Enter target password : ")
max_length=int(input("Enter max length : "))
password_hint(target_password, max_length)

'''
import string
import itertools

def password(target, length):

  charcter=string.ascii_uppercase+string.ascii_lowercase+string.digits


  for i in itertools.product(charcter,repeat=length):
    p="".join(i)


    if(p==target):
      print("corrct")



target = input("jfh")  # Get user input for target
length = int(input("KJ") ) # Get user input for length
password(target, length) 
