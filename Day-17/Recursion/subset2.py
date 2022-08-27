# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        totalSubset = []
        
        def recSol(nums,index,subset):
            
            if index == len(nums):
                totalSubset.append(subset)
                return
                
            recSol(nums,index+1,subset)
            newSubset = subset[:]
            newSubset.append(nums[index])
            recSol(nums,index+1,newSubset)
            
        recSol(nums,0,[])
        
        return set(tuple(sorted(i)) for i in totalSubset)
            
            
        
        
        
        