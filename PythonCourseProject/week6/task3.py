"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        count = 0
        current = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current += 1
                count += current
            else:
                current = 0

        return count
