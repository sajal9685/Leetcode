numbers = [2,3,4]
target = 6
i=0

while i<=len(numbers):
    j=i+1 
    while j<=len(numbers)-1: 
        if numbers[i]+numbers[j]==target:
            print([i+1,j+1])
        j+=1
    i+=1    

"""
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in dict:
                return [dict[rem]+1,i+1]
            dict[nums[i]]=i    
         
         """


            








    

