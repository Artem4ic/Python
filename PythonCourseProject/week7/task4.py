"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/submissions/1461933325/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        cumulative_sum = 0
        sum_count = {0: 1}

        for num in nums:
            cumulative_sum += num

            if (cumulative_sum - goal) in sum_count:
                count += sum_count[cumulative_sum - goal]

            if cumulative_sum in sum_count:
                sum_count[cumulative_sum] += 1
            else:
                sum_count[cumulative_sum] = 1

        return count
