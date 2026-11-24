# Problem: 344. Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)
# Runtime: 4 ms (Beats 41.95%) | Memory: 19.41 MB (Beats 96.04%)

class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
