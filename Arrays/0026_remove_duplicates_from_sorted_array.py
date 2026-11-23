# Problem: 26. Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Pattern: Two Pointers
# Time: O(n)
# Space: O(1)
# Runtime: 2ms (Beats 76.40%) | Memory: 13.44MB (Beats 73.35%)


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        slow=0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
