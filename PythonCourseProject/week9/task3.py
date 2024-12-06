"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/replace-the-substring-for-balanced-string/submissions/1470458607/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def balancedString(self, s):
        n = len(s)
        target_count = n // 4

        count = {"Q": 0, "W": 0, "E": 0, "R": 0}
        for char in s:
            count[char] += 1

        if all(count[char] <= target_count for char in count):
            return 0

        excess = {char: max(0, count[char] - target_count) for char in count}

        left = 0
        min_length = n

        for right in range(n):
            if s[right] in excess:
                excess[s[right]] -= 1

            while all(excess[char] <= 0 for char in excess):
                min_length = min(min_length, right - left + 1)
                if s[left] in excess:
                    excess[s[left]] += 1

                left += 1

        return min_length
