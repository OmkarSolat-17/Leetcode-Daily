# Problem: 283. Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)
# Runtime: 11ms (Beats 21.67%) | Memory: 13.49MB (Beats 65.49%)


class Solution(object):
    def moveZeroes(self, nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1