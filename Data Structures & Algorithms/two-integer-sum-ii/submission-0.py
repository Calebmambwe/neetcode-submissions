'''
input = array (increasing order)
output = indcies (1-indexed) [index1,index2] == target number

contraints 

index1 < index2 cannot be equal cannot use the same element twice
O(1) soluiton 

how do we use the sorted order ?

traverse the array 

so we can have the target then look at the numbers that come before then subtract the number from the potion 


 numbers = [1,3,4,5,7,9], target = 8
 are we alway sgurantede that we have a match in pair?

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l +1, r + 1]
        return []

        