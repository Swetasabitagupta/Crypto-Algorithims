"""
Usage:  If the text is encrypted: it'll decrypt it; else: it will encrypt it 
"""
text='Who am I?'
strOut = ''
for i  in text:
    if (ord(i)>64 and ord(i)<78) ^ (ord(i)>96 and ord(i)<110):
        strOut+=chr(ord(i)+13)
    elif ((ord(i)>77 and ord(i)<91) ^ (ord(i)>109 and ord(i)<123)):
        strOut+=chr(ord(i)-13)
    else:
        strOut+=i
print(strOut)
