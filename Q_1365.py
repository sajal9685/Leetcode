nums=[8,1,2,2,3]
new=[]

for i in range(len(nums)):
    n=0
    for j in range(len(nums)):
        if nums[j]<nums[i]:
    
            n+=1
    new.append(n)
print(new)        
    

