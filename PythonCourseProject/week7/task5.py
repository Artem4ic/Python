"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-number-of-nice-subarrays/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        return count_at_most(nums, k) - count_at_most(nums, k - 1)


def count_at_most(nums, k):
    left = 0
    count = 0
    odd_count = 0

    for right in range(len(nums)):
        if nums[right] % 2 != 0:
            odd_count += 1

        while odd_count > k:
            if nums[left] % 2 != 0:
                odd_count -= 1
            left += 1

        count += right - left + 1

    return count
