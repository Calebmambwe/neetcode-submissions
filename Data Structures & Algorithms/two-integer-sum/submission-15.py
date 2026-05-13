from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        MyNumber = {}
        for i in range(len(nums)):
            findMe = target - nums[i]
            if findMe in MyNumber:
                return [MyNumber[findMe], i]
            MyNumber[nums[i]] = i 
        return []
            

'''

Input: 
nums = [3,4,5,6], target = 7
          i
for loop
findMe = target - i 
if findMe in My numbers 
    return [index in dict, curent i] 
store index in dict
add i = 0 to MyNumber
return [-1,-1]

MyNumber =[3: i=0
           4: i=1 
           5: i=2
           6: i=3      
] 


Output: [0,1]
findme = 4
MyNumber = [3]
'''




        