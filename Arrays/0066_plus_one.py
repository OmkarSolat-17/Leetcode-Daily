# Problem: 66. Plus One
# Link: https://leetcode.com/problems/plus-one/
# Difficulty: Easy
# Pattern: Math / Carry
# Time: O(n)
# Space: O(n) worst case
# Runtime: 0 ms (Beats 100.00%) | Memory: 12.06 MB (Beats 88.46%)

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
