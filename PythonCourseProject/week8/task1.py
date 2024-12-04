"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/continuous-subarrays/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""

from collections import deque


class Solution(object):
    def continuousSubarrays(self, nums):
        n = len(nums)
        start = 0
        total_count = 0

        max_deque = deque()
        min_deque = deque()

        for end in range(n):
            while max_deque and nums[max_deque[-1]] <= nums[end]:
                max_deque.pop()
            max_deque.append(end)

            while min_deque and nums[min_deque[-1]] >= nums[end]:
                min_deque.pop()
            min_deque.append(end)

            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                start += 1
                if max_deque[0] < start:
                    max_deque.popleft()
                if min_deque[0] < start:
                    min_deque.popleft()

            total_count += end - start + 1

        return total_count
