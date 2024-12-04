"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/get-equal-substrings-within-budget/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        left = 0
        total_cost = 0
        max_length = 0

        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            total_cost += cost

            while total_cost > maxCost:
                total_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
