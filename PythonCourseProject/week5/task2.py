"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-consecutive-sequence/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)

        return max_length
