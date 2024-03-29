# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        
        for i in range(numRows) : 
            
            ans = [1] * (i + 1)
            
            for j in range(1,i):
                ans[j] = output[i-1][j] + output[i-1][j-1]
            
            output.append(ans)
                
        
        return output
        