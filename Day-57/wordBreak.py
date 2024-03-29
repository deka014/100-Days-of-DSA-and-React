# 139. Word Break
# Medium
# 14.6K
# 613
# Companies

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

 

# Constraints:

#     1 <= s.length <= 300
#     1 <= wordDict.length <= 1000
#     1 <= wordDict[i].length <= 20
#     s and wordDict[i] consist of only lowercase English letters.
#     All the strings of wordDict are unique.

# Accepted
# 1.4M
# Submissions
# 3M
# Acceptance Rate
# 45.7%


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        wordDict = set(wordDict)
        def recsol(start,end):
            if start == end == len(s) :
                return True
            
            if end >= len(s) :
                return False 
            
            boolfromfuture = False
            
            if s[start:end+1] in wordDict:
                boolfromfuture = recsol(end+1,end+1)
            
            return boolfromfuture or recsol(start,end+1)

        
        return recsol(0,0)




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        wordDict = set(wordDict)
        memo = [[None] * len(s) for i in range(len(s))]
        def recsol(start,end):
            if start == end == len(s) :
                return True
            
            if end >= len(s) :
                return False 
            
            boolfromfuture = False

            if memo[start][end] != None :
                return memo[start][end]
            
            if s[start:end+1] in wordDict:
                boolfromfuture = recsol(end+1,end+1)
                
            memo[start][end] = boolfromfuture or recsol(start,end+1)

            return memo[start][end]

        
        return recsol(0,0)



