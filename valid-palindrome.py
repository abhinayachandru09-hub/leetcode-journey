#LeetCode #125: Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""

        for char in s:
            if char.isalnum():
                x+=char.lower()

        return x==x[::-1]