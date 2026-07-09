import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = Counter(nums)
        res = list(most_freq.items())
        max_heap = [(-val, key) for key, val in res]
        heapq.heapify(max_heap)
        
        result = []
        for i in range(k):
            re = heapq.heappop(max_heap)
            result.append(re[1])
        return result 




