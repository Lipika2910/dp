
def encrypt(text,shift_value):
    result=" "

    for i in range(0,len(text)):
        if(text[i].isupper()):
            result+=chr((ord(text[i])+shift_value-65)%26+65)
        elif(text[i].islower()):
            result+=chr((ord(text[i])+shift_value-97)%26+97)
        else:
            result+=" "


    return result


def decrypt(text,shift_value):
    result=" "

    for i in range(0,len(text)):
        if(text[i].isupper()):
            result+=chr((ord(text[i])-shift_value+65)%26+65)
        elif(text[i].islower()):
            result+=chr((ord(text[i])-shift_value-97)%26+97)
        else:
            result+=" "


    return result



print("Option 1 : encryption\n")
print("Option 2 : decryption\n")

option=int(input("choose option : "))


text=str(input("Enter text : "))
shift_value=int(input("Enter shift value : "))

if (option==1):
    print("Encrypted text : ",encrypt(text, shift_value))

if (option==2):
    print("Decrypted text : ",decrypt(text, shift_value))
