# Problem: 242. Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Pattern: Hash Map (frequency counting)
# Time: O(n)
# Space: O(n)
# Runtime: 14ms (Beats 87.27%) | Memory: 12.10MB (Beats 98.65%)


# ── Approach 1: Two Hash Maps ──────────────────────────────────────
class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for a in s:
            if a in d1:
                d1[a] += 1
            else:
                d1[a] = 1

        for b in t:
            if b in d2:
                d2[b] += 1
            else:
                d2[b] = 1

        return d1 == d2


# ── Approach 2: Single Hash Map ────────────────────────────────────
# Runtime: 13ms (Beats 90.27%) | Memory: 12.32MB (Beats 87.46%)

# class Solution(object):
#     def isAnagram(self, s, t):
#
#         if len(s) != len(t):
#             return False
#
#         d = {}
#
#         for a in s:
#             if a in d:
#                 d[a] += 1
#             else:
#                 d[a] = 1
#
#         for b in t:
#             if b in d and d[b] > 0:
#                 d[b] -= 1
#             else:
#                 return False
#
#         return True