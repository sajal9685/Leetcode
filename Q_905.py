nums = [3,1,2,4]    

start=0
for i in range(len(nums)):
    if nums[i]%2==0:
        temp=nums[i]
        nums[i]=nums[start]
        nums[start]=temp
        start+=1
print(nums)        
