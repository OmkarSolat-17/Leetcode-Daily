# Problem: 125. Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)
# Runtime: 11ms (Beats 93.42%) | Memory: 12.65MB (Beats 70.99%)


class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True