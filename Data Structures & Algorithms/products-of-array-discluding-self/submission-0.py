'''


Input: nums = [1,2,4,6]

return arrray Output: [48,24,12,8] 
                        i where is the product of all elements of. nums execept its current position nums[i] 

Input: nums = [1,2,4,6]
  
            48, 24,12, 8
    oh this is n2 solution 

            always multiply the numbers just skip the current 
    we need a running product 

    result array start with 1 
    loop through the array in range(len(nums))
       loop each element len(nums)
            skip j index
        if i == j:
            continue 
        result[i] *= nums[i]
        skip nums[j] = j can be got. from result array and continue

        result = []
        result += [[1] for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue 
                result[i] *= nums[j] 
        return result 

...
...    
      
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    result[i] *= nums[j]
        return result 
        