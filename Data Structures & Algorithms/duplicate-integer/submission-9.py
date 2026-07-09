class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # res = set()

        # for num in nums:
        #     if num in res:
        #         return True
        #     res.add(num)
        # return False  

        '''
        [1, 2, 3, 3]
        i  j
        '''
        
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True 
        return False