"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/additive-number/?envType=problem-list-v2&envId=string&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)

        def is_valid_sequence(first, second, start_index):
            while start_index < n:
                next_number = str(int(first) + int(second))
                if not num.startswith(next_number, start_index):
                    return False
                start_index += len(next_number)
                first, second = second, next_number

            return True

        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == "0") or (
                    len(second) > 1 and second[0] == "0"
                ):
                    continue
                if is_valid_sequence(first, second, j):
                    return True

        return False
