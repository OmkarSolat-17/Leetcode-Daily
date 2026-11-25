# Problem: 28. Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy
# Pattern: String Matching (Brute Force)
# Time: O(n*m)
# Space: O(m)
# Runtime: 0 ms (Beats 100.00%) | Memory: 12.10 MB (Beats 96.47%)

class Solution(object):
    def strStr(self, haystack, needle):
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1