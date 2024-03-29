# 1793. Maximum Score of a Good Subarray
# Hard
# 1.4K
# 38
# Companies

# You are given an array of integers nums (0-indexed) and an integer k.

# The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

# Return the maximum possible score of a good subarray.

 

# Example 1:

# Input: nums = [1,4,3,7,4,5], k = 3
# Output: 15
# Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 

# Example 2:

# Input: nums = [5,5,4,5,4,1,1,1], k = 0
# Output: 20
# Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

 

# Constraints:

#     1 <= nums.length <= 105
#     1 <= nums[i] <= 2 * 104
#     0 <= k < nums.length

# Accepted
# 44K
# Submissions
# 71.7K
# Acceptance Rate
# 61.4%

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        

        # 1 3 3 7 4 4  

        ans = nums[k]
        i = k
        j = k
        currmin = nums[k]

        while i>0 or j<len(nums)-1 :

            left = nums[i-1] if i>0 else 0
            right = nums[j+1] if j < len(nums)-1 else 0

            if left>right:
                i-=1
                currmin = min(currmin,left)
            else :
                j+=1
                currmin = min(currmin,right)

            ans = max(ans,currmin * (j-i+1))

        return ans