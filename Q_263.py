# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
n=6
li=[]
for i in range(1,11):
    if n % i==0:
        li.append(i)
print(li)
for i in range(0,len(li)):
        if li[i]!=2 or li[i]!=3 or li[i]!=5:
            print(False)
            break
        else:
            print(True) 
