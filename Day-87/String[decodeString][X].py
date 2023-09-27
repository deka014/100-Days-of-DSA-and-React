# 880. Decoded String at Index
# Medium
# 2.1K
# 296
# Companies

# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

#     If the character read is a letter, that letter is written onto the tape.
#     If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

# Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

# Example 1:

# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".

# Example 2:

# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5th letter is "h".

# Example 3:

# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".

 

# Constraints:

#     2 <= s.length <= 100
#     s consists of lowercase English letters and digits 2 through 9.
#     s starts with a letter.
#     1 <= k <= 109
#     It is guaranteed that k is less than or equal to the length of the decoded string.
#     The decoded string is guaranteed to have less than 263 letters.

# Accepted
# 74.7K
# Submissions
# 213.4K
# Acceptance Rate
# 35.0%

class Solution:
    def decodeAtIndex(self, inputString: str, k: int) -> str:
        decoded_length = 0  # Total length of the decoded string

        for char in inputString:
            if char.isdigit():
                # If the character is a digit, update the decoded length accordingly
                decoded_length *= int(char)
            else:
                # If the character is a letter, increment the decoded length
                decoded_length += 1

        # Traverse the input string in reverse to decode and find the kth character
        for i in range(len(inputString) - 1, -1, -1):
            current_char = inputString[i]

            if current_char.isdigit():
                # If the character is a digit, adjust the length and k accordingly
                decoded_length //= int(current_char)
                k %= decoded_length
            else:
                # If the character is a letter, check if it's the kth character
                if k == 0 or decoded_length == k:
                    return current_char  # Return the kth character as a string

                decoded_length -= 1

        return ""  # Return an empty string if no character is found