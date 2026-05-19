nums = [1,1,1,2,2,3]
n=len(nums)
if n<=2:
    print (n)
k=1
for i in range (2,n):
    if nums[i]!=nums[k-1]:
        k+=1
        nums[k]= nums[i]
    print(k+1)