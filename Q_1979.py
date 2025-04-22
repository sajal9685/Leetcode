nums =[2,5,6,9,10]
nums.sort()
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.
for index in nums:
    new=[nums[0],nums[-1]]
list=[]
for i in range(1,1001):
    if new[0]%i==0 and new[1]%i==0:
        list.append(i)
print(f"output:{list[-1]}")        
         
      
