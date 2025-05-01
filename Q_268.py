# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range 
# [0,3]. 2 is the missing number in the range since it does not appear in nums.
nums = [9,6,4,2,3,5,7,0,1]
nums.sort()
li=[]
found=False
for i in range(0,len(nums)+1):
    li.append(i)
for i in range(0,len(nums)):
    if nums[i]!=li[i]:
        found=True
        print(i)
if not found:
    print(li[i+1])         


        

