from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_hash = defaultdict(list)

        result = []
        for str1 in strs:
            ana_hash[tuple(sorted(str1))].append(str1)
        
        for key, val in ana_hash.items():
            result.append(val)
        
        return result 