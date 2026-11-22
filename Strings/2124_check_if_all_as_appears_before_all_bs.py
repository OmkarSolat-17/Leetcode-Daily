# Problem: 2124. Check if All A's Appears Before All B's
# Link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Difficulty: Easy
# Pattern: String / Substring Check
# Time: O(n)
# Space: O(1)
# Runtime: 0ms (Beats 100.00%) | Memory: 12.02MB (Beats 83.23%)


class Solution(object):
    def checkString(self, s):
        return "ba" not in s