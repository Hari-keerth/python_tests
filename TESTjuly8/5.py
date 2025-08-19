# 5
word=input("enter a string :")
new=""
for i in range(0,len(word)):
    if i % 2 ==0 and word[i] in "aeiou":
        new=new+"#"
    elif i % 2 ==0:
        new=new+"*"
    else:
        new=new+word[i]
print(new)