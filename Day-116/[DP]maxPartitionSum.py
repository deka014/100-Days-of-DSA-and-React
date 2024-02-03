# 1043. Partition Array for Maximum Sum
# Medium
# 4K
# 291
# Companies

# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]

# Example 2:

# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83

# Example 3:

# Input: arr = [1], k = 1
# Output: 1

 

# Constraints:

#     1 <= arr.length <= 500
#     0 <= arr[i] <= 109
#     1 <= k <= arr.length

# Accepted
# 111.5K
# Submissions
# 150.6K
# Acceptance Rate
# 74.1%


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = {}


        def rec(index):

            if index == len(arr):
                return 0

            if index in dp :
                return dp[index]

            maxnum = float("-inf")
            partlen = 0
            totalsum = 0

            for i in range(index,min(len(arr),index+k)):

                partlen+=1
                maxnum = max(maxnum,arr[i])

                totalsum = max(totalsum,(maxnum)*partlen + rec(i+1))

            dp[index] = totalsum

            return totalsum

        
        return rec(0)