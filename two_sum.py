class Solution:
    def twoSum(self, nums, target):
        
        #Iterate through each element in the list
        for i in range(len(nums)):
            
            #For each element, check the remaining elements
            for j in range(i + 1, len(nums)):
                
                #Check if the sum of two numbers equals target
                if nums[i] + nums[j] == target:
                    
                    #If condition is satisfied, return their indices
                    return [i, j]
