# Problem: 217. Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Pattern: Hash Set
# Time: O(n)
# Space: O(n)
# Runtime: 32ms (Beats 47.51%) | Memory: 25.92MB (Beats 34.13%)


class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False