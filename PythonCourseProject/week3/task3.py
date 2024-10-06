"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/rotate-image/?envType=problem-list-v2&envId=array&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # print(matrix)
        for i in range(n):
            matrix[i].reverse()
