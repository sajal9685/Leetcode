# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
li=[]
set1=set(nums1)
set2=set(nums2)
inter=(set1.intersection(set2))
for i in inter:
    print (i,type(i))
    li.append(i)

print(li)