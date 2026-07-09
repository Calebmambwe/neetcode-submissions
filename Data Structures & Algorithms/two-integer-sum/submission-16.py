class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        my_nums = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in my_nums:
                return sorted([my_nums[compliment],i])
            my_nums[nums[i]] = i
        return []