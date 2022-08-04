# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        arrStack = []
        temp = ""
        s+= " "
        for i in s :
            
            if i == " " :
                
                if temp :
                    arrStack.append(temp)
                temp = ""
            
            else :
                temp += i
                
        print(arrStack)
        
        while len(arrStack) > 1 :
            output+= arrStack.pop()
            output+= " "
        output+= arrStack.pop()
        return output
            
                
            
class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.split()
        arr.reverse()
        output = " ".join(arr)
        
        return output