# 1287. Element Appearing More Than 25% In Sorted Array
# Easy
# 1.4K
# 66
# Companies

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

# Example 2:

# Input: arr = [1,1]
# Output: 1

 

# Constraints:

#     1 <= arr.length <= 104
#     0 <= arr[i] <= 105

# Accepted
# 156.7K
# Submissions
# 256.9K
# Acceptance Rate
# 61.0%


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        limit = int(0.25*len(arr))

        prev = arr[0]
        count = 1

        for num in arr[1:]:

            if num == prev :
                count+=1
            else :
                prev = num
                count = 1
            
            if count > limit :
                break
        
        return prev