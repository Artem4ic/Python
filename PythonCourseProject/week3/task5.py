"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sort-colors/?envType=problem-list-v2&envId=array&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
