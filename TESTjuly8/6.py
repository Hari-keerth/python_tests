# 6
# word=input("Enter a string :")
# new=""
# j=0
# for i in range(0,len(word)):
#     if word[i] not in new:
#          j+=1
#          new=new+word[i]
#          print(f"{word[i]}:{j}")
#     else:
#          j=0
#   OUTPUT
#   ------
# Enter a string :apple
# a:1
# p:2
# l:1
# e:2

# =============================
#              OR
# =============================

word=input("Enter a string :")
new=""
for i in word:
     if i not in new:
          count=1
          new+=i
          for j in word[word.index(i)+1:]:
            if j==i:
             count+=1
          print(i,count)
#   OUTPUT
#   ------
# Enter a string :apple
# a 1
# p 2
# l 1
# e 1

#Enter a string :hello   world
# h 1
# e 1
# l 3
# o 2
#   3
# w 1
# r 1
# d 1