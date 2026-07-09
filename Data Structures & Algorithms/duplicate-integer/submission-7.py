class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for num in nums:
            if num in res:
                return True
            res.add(num)
        return False  
        # for i in range(len(nums)):
        #     for j in range( i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True 
        # return False   