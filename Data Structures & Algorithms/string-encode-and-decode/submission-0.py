
'''
An Algo to encode a list of strings to a string

iterate through the list of strings 
find a way to distinguish each string (delimiter)
count how many characters it is 

Input: dummy_input = ["Hello","World"]
                       i   j
encode 

    result = ""
    for to iterate the array 
       while j: 
          once you have that information 
          add the number of string chars 
            cound with two pointer 
            i += 1 
            result += # + char(i + 1) + str[:i]

single_string = "#5Hello#5World"

'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for strs1 in strs:
            num = len(strs1)
            result += str(num) + "#" + strs1
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the '#' that terminates the length number
            j = i
            #find the number first eg "10"
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # the actual string runs from j+1 to j+1+length
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
