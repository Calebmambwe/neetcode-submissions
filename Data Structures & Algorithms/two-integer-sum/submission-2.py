class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #[ints] , target 
        #retuen i and j 
        #such that nums[i] + nums[j] == target 

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return [-1, -1]

        '''  nums=[2,5,5,11] 
                   i
                     j
        
        
        
        
        '''

        