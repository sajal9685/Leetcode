# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.
nums = [1,1,1,3,3,4,3,2,4,2]
nums.sort()

for i in range(0,len(nums)-1):
    if nums[i]==nums[i+1]:
        print (True)
        break
else:
    print(False)        