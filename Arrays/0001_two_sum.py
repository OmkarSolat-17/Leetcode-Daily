# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Pattern: Hash Map (complement lookup)
# Time: O(n)
# Space: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Store each number's index in a hash map. For every element,
        check if target - num was already seen. O(n) time, O(n) space."""
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# ── Tests ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]

    print("All tests passed! ✅")