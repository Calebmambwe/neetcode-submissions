from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = sorted(s)
        string2 = sorted(t)

        return string1 == string2 

        


        
        