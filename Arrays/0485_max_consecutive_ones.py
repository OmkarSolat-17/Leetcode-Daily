# Problem: 485. Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: Easy
# Pattern: Linear Scan
# Time: O(n)
# Space: O(1)
# Runtime: 14 ms (Beats 91.30%) | Memory: 13.29 MB (Beats 95.45%)

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c = 0
        max_c = 0
        for n in nums:
            if n == 1:
                c += 1
                if c > max_c:
                    max_c = c
            else:
                c = 0
        return max_c
