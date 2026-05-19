nums1 = [1,2,3]
nums2 = [2,4]
i=0
j=0
while i<len(nums1) and j<len(nums2):
    if nums1[i]==nums2[j]:
        print (nums1[i])
    elif nums1[i]<nums2[j]:
        i+=1
    else :
        j+=1
                    