class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #data structure that doesnt allow duplicates
        numsList = set()

        for num in nums:
            if num in numsList:
                return True 
            numsList.add(num)
        return False
        