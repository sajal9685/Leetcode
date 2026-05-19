nums = [1,1,2]

k=0
for i in range (len(nums)):
    if nums[i]!=nums[k]:
        k+=1
        nums[k]= nums[i]
    print(k+1)    