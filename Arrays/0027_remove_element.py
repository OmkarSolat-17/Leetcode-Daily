# Problem: 27. Remove Element
# Link: https://leetcode.com/problems/remove-element/
# Difficulty: Easy
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)
# Runtime: 0ms (Beats 12.23%) | Memory: 12.23MB (Beats 53.69%)


class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] == val:
                if nums[right] != val:
                    nums[left] = nums[right]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return left