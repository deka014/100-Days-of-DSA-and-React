# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons
# Hard
# 875
# 52
# Companies

# You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

# You should build the array arr which has the following properties:

#     arr has exactly n integers.
#     1 <= arr[i] <= m where (0 <= i < n).
#     After applying the mentioned algorithm to arr, the value search_cost is equal to k.

# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

# Example 1:

# Input: n = 2, m = 3, k = 1
# Output: 6
# Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

# Example 2:

# Input: n = 5, m = 2, k = 3
# Output: 0
# Explanation: There are no possible arrays that satisify the mentioned conditions.

# Example 3:

# Input: n = 9, m = 1, k = 1
# Output: 1
# Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

 

# Constraints:

#     1 <= n <= 50
#     1 <= m <= 100
#     0 <= k <= n

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp = [[[None] * (n+1) for _ in range(m + 1)] for _ in range(k + 1)]

        def rec(index, currMax, currCost):
            if currCost > k:
                return 0

            if index == n:
                if currCost == k:
                    return 1
                else:
                    return 0

            if dp[currCost][currMax][index] != None:
                return dp[currCost][currMax][index]

            ans = 0

            for i in range(1, m + 1):
                if i > currMax:
                    ans += rec(index + 1, i, currCost + 1)
                else:
                    ans += rec(index + 1, currMax, currCost)

            dp[currCost][currMax][index] = ans
            return ans
    
        return rec(0, -1, 0) % (10**9+7)
