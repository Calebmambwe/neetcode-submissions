from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        string1 = sorted(s)
        string2 = sorted(t)
        for i in range(len(s)):
            if string1[i] != string2[i]:
                return False  
        return True 

        


        
        