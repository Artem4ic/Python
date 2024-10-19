"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/powerful-integers/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        powerful_integers = set()

        if x == 1:
            x_powers = [1]
        else:
            x_powers = []
            power = 1
            while power <= bound:
                x_powers.append(power)
                power *= x

        if y == 1:
            y_powers = [1]
        else:
            y_powers = []
            power = 1
            while power <= bound:
                y_powers.append(power)
                power *= y

        for xi in x_powers:
            for yj in y_powers:
                if xi + yj <= bound:
                    powerful_integers.add(xi + yj)

        return list(powerful_integers)
