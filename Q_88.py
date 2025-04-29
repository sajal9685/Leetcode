# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1=[-1,0,0,3,3,3,0,0,0]
m=6
nums2=[1,2,2]
n=3
i=m    
for i in range(n):
    nums1[m+i]=nums2[i]
nums1.sort()
print(nums1)