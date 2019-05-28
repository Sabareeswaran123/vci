k=input()
v=['a','e','i','o','u','A','E','I','O','U']
if (ord(k)>64 and ord(k)<91) or (ord(k)>96 and ord(k)<123):
    if k in v:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
