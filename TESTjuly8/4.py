# 4
word=input("Enter a string :")#python
new=""
count=0
for i in word.lower():
    if i not  in "aeiou":
        new=new+i
    elif i in "aeiou":
        count+=1
print(f"The orginal string is --> {word} \nThe new string is ---> {new} \ncount of vowels is {count}")


