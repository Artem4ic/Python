"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/fraction-to-recurring-decimal/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        if (numerator < 0) ^ (denominator < 0):
            sign = "-"
        else:
            sign = ""

        num, denom = abs(numerator), abs(denominator)
        integer_part = num // denom
        remainder = num % denom

        if remainder == 0:
            return sign + str(integer_part)

        result = sign + str(integer_part) + "."
        remainder_map = {}
        fractional_part = ""

        index = 0
        while remainder != 0:
            if remainder in remainder_map:
                start_index = remainder_map[remainder]
                fractional_part = (
                    fractional_part[:start_index]
                    + "("
                    + fractional_part[start_index:]
                    + ")"
                )
                break

            remainder_map[remainder] = index
            remainder *= 10
            fractional_part += str(remainder // denom)
            remainder %= denom

            index += 1

        return result + fractional_part
