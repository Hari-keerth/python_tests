# 3
num=int(input("Enter a number :"))
sum=0
temp=num
v=len(str(num))
while num>0:
    digit=num%10
    sum=sum+digit**v
    num=num//10
if sum==temp:
    print("Is Armstrong")
else:
    print("Is  not Armstrong")