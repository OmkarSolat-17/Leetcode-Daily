# LeetCode Daily

Daily LeetCode practice in Python, organized by topic. Each solution includes the approach, time complexity, and space complexity.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116?style=flat-square&logo=leetcode&logoColor=black)
![Status](https://img.shields.io/badge/Status-Active-2EA44F?style=flat-square)

## Overview

This repository tracks my daily DSA practice on LeetCode. Each problem is saved in the folder for its main topic, with a short explanation of the approach and its complexity. I'm working toward AI/ML engineering roles, so the aim is to build solid fundamentals that carry over to algorithm-heavy interviews.

## Repository Structure

```text
LeetCode-Daily/
├── Arrays/
│   ├── 0001_two_sum.py
│   └── ...
└── README.md
```

Topics are added as I start them. The full roadmap is in the Topic Coverage table below.

Files are named `NNNN_problem_name.py`, where `NNNN` is the LeetCode problem number.

## Solution Format

Every file follows the same layout:

```python
# Problem: 1. Two Sum
# Difficulty: Easy
# Pattern: Hash Map (complement lookup)
# Time: O(n)
# Space: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
```

## Progress

Last updated: 2026-11-18

| Difficulty | Solved |
| :--------: | :----: |
|    Easy    |   1    |
|   Medium   |   0    |
|    Hard    |   0    |
| **Total**  | **1**  |

### Topic Coverage

| Topic               | Solved | Status      |
| ------------------- | :----: | ----------- |
| Arrays              |   1    | In progress |
| Strings             |   0    | Planned     |
| Hashing             |   0    | Planned     |
| Two Pointers        |   0    | Planned     |
| Sliding Window      |   0    | Planned     |
| Binary Search       |   0    | Planned     |
| Stack and Queue     |   0    | Planned     |
| Linked Lists        |   0    | Planned     |
| Trees               |   0    | Planned     |
| Graphs              |   0    | Planned     |
| Backtracking        |   0    | Planned     |
| Greedy              |   0    | Planned     |
| Dynamic Programming |   0    | Planned     |

## Workflow

For each problem:

1. Read the statement and note the constraints.
2. Identify the pattern before writing code.
3. Write a working solution, then optimize it.
4. Record time and space complexity in the file header.
5. Commit with the problem number and title.

## Commit Convention

```text
Add 0001 Two Sum (Easy, Arrays)
```

## Running Locally

```bash
git clone https://github.com/OmkarSolat-17/LeetCode-Daily.git
cd LeetCode-Daily
python Arrays/0001_two_sum.py
```

## Author

**Omkar Solat** -
B.Tech CSE (AI/ML), 4th Semester

[GitHub](https://github.com/OmkarSolat-17) · [LinkedIn](https://www.linkedin.com/in/omkar-solat-os17/) · [LeetCode](https://leetcode.com/u/omkarsolat_17/) · [Portfolio](https://omkarsolat-17.github.io/portfolio/)
