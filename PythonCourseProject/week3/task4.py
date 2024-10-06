"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/set-matrix-zeroes/?envType=problem-list-v2&envId=array&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
