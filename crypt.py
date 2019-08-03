#Ceaser Cipher


#encryption code
def encryption(text, k):
    result = " "
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result


#decryption code
def decryption(text, k):
    result = " "
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)
        else:
            result += chr((ord(char) - k - 97) % 26 + 97)
    return result


print("Enter The Text")
text = input("input text")
k = int(input("Shift"))
print("Select Algorithim")
print("1.Encryption_Algorithim")
print("2.Decryption_Algorithm")

Choice = int(input("Enter Choice(1/2)"))

if Choice == 1:
    print("Cipher:" + encryption(text, k))
elif Choice == 2:
    print("Plain text:" + decryption(text, k))
else:
    exit()





