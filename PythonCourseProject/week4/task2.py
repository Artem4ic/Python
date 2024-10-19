"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/triangle/?envType=problem-list-v2&envId=array&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def minimumTotal(self, triangle):
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )
        return triangle[0][0]
