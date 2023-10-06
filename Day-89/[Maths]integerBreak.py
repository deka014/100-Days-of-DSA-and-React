# 343. Integer Break
# Medium
# 4.7K
# 411
# Companies

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:

# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 

# Constraints:

#     2 <= n <= 58

class Solution:
    def integerBreak(self, n: int) -> int:

        ans = 1
        
        if n <= 3 :
            return n-1

        while n > 0 :

            if n-3 > 1 :
                ans*=3
                n-=3
            else :
                ans*=n
                return ans

        return ans


