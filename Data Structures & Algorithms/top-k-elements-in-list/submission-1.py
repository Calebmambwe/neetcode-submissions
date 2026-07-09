from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_k = Counter(nums)

        res = sorted(my_k.items(), key=lambda item: item[1], reverse = True)
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result



