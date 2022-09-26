class Solution:
   def twoSum(self,nums, target):
      
    for index in range(len(nums)):

     for index2 in range(index+1,len(nums)):

        if(nums[index]+nums[index2]==target):
         value = [index,index2]
         return value
        
