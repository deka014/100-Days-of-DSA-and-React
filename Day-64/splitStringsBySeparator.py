# 2788. Split Strings by Separator
# Easy
# 98
# 2
# Companies

# Given an array of strings words and a character separator, split each string in words by separator.

# Return an array of strings containing the new strings formed after the splits, excluding empty strings.

# Notes

#     separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
#     A split may result in more than two strings.
#     The resulting strings must maintain the same order as they were initially given.

 

# Example 1:

# Input: words = ["one.two.three","four.five","six"], separator = "."
# Output: ["one","two","three","four","five","six"]
# Explanation: In this example we split as follows:

# "one.two.three" splits into "one", "two", "three"
# "four.five" splits into "four", "five"
# "six" splits into "six" 

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        
        
        for word in words :
            temp = ""
            for i in range(len(word)) :
                if word[i] != separator :
                    temp += word[i]
                elif word[i] == separator : 
                    if len(temp) > 0 :
                        result.append(temp)
                        temp = ""
            if len(temp) > 0 :
                result.append(temp)
                
        return result