#LeetCode #3:Length Of Longest Substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # stores character and its latest index
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            # If character already exists in current window
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update character's latest position
            char_index[char] = right

            # Calculate window length
            length = right - left + 1

            # Update maximum length
            max_length = max(max_length, length)

        return max_length