from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a hashmap count
        dictionary = defaultdict(int)
        dictionary2 = defaultdict(int)
        
        for char in s:
            dictionary[char] += 1
        for char in t:
            dictionary2[char] += 1
        return dictionary == dictionary2 

        


        
        