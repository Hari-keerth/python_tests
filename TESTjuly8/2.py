# 2
string=input("Enter a string :")
vowel=0
consonants=0
digit=0
special=0
for i in string:
    if i in "aeiou":
        vowel+=1
    elif i not in "aeiou" and i.isalpha() == True:
        consonants+=1
    elif i.isdigit()==True:
        digit+=1
    else:
        special+=1
print(f"vowels={vowel}. Consonants={consonants} .Digits={digit}.  Special={special} ")