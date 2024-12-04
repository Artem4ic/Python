"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def maxSum(self, nums, m, k):
        n = len(nums)
        if n < k:
            return 0

        max_sum = 0
        current_sum = 0
        freq = {}
        distinct_count = 0

        for i in range(k):
            current_sum += nums[i]
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
                distinct_count += 1

        if distinct_count >= m:
            max_sum = current_sum

        for i in range(k, n):
            outgoing = nums[i - k]
            current_sum += nums[i] - outgoing

            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
                distinct_count -= 1

            incoming = nums[i]
            if incoming in freq:
                freq[incoming] += 1
            else:
                freq[incoming] = 1
                distinct_count += 1

            if distinct_count >= m:
                max_sum = max(max_sum, current_sum)

        return max_sum
