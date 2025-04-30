# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.
#Q_217
nums1 = [1,1,1,3,3,4,3,2,4,2]
nums1.sort()

for i in range(0,len(nums1)-1):
    if nums1[i]==nums1[i+1]:
        print (True)
        break
else:
    print(False)      
# Input: nums = [1,2,3,1], k = 3
# Output: true  
#Q_219
nums = [1,0,1,1]
k = 1
found = False
for i in range(0,len(nums)-1):
    j=i+1
    for j in range (j,len(nums)):
        if nums[i]==nums[j]:
            if abs(i-j)<=k:
                print(True,i,j)
                found = True
                break
    if found:
        break
if not found:
    print(False)