# Problem: 169. Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Pattern: Boyer-Moore Voting Algorithm
# Time: O(n)
# Space: O(1)
# Runtime: 11ms (Beats 81.17%) | Memory: 13.04MB (Beats 99.78%)


# Boyer–Moore majority vote algorithm
class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate