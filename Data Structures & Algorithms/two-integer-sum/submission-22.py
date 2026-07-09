class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        i = 0 
        j = len(nums) - 1 
        new_array = []
        for n in range(len(nums)):
            new_array.append((nums[n],n))
        
        new_array.sort()

        while i < j:
            if (new_array[i][0] + new_array[j][0]) == target:
                return sorted([new_array[i][1], new_array[j][1]]) 
            elif (new_array[i][0] + new_array[j][0]) < target:
                i += 1
            else:
                j -= 1
        return []

