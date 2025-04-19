nums=int(input([]))
k=int(input())
count=0
i=0
j=1
while i<=6:
    j=i+1
    while j<=6:
        if nums[j]==nums[i]:
             mul=i*j
             print(i,j,mul)
             if mul%k==0:
                count+=1
                j+=1
    i+=1
print(count)    
