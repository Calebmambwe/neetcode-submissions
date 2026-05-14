from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        we need a dictionary data structure  

        store the key = whichis the number , the value which is the count 
        sort the results by count 
        print k and appedn to the array 
        
        '''
        result = []
        myStore = defaultdict(int)

        for num in nums:
            myStore[num] += 1 
        sorted_items = sorted(myStore.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sorted_items[i][0])
        return result 
        