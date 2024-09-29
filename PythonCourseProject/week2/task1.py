"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-number/?envType=problem-list-v2&envId=string&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def largestNumber(self, nums):
        nums_str = list(map(str, nums))
        n = len(nums_str)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        largest_num = "".join(nums_str)
        if largest_num[0] == "0":
            return "0"

        return largest_num


# print(largestNumber([10, 2]))
# print(largestNumber([3, 30, 34, 5, 9]))
