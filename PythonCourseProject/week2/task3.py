"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator-ii/?envType=problem-list-v2&envId=string&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def calculate(self, s):
        stack = []
        current_number = 0
        last_operator = "+"
        s = s.replace(" ", "")

        for i in range(len(s)):
            char = s[i]

            if char.isdigit():
                current_number = current_number * 10 + int(char)

            if char in "+-*/" or i == len(s) - 1:
                if last_operator == "+":
                    stack.append(current_number)
                elif last_operator == "-":
                    stack.append(-current_number)
                elif last_operator == "*":
                    stack[-1] = stack[-1] * current_number
                elif last_operator == "/":
                    if (
                        stack[-1] // current_number < 0
                        and stack[-1] % current_number != 0
                    ):
                        stack[-1] = stack[-1] // current_number + 1
                    else:
                        stack[-1] = stack[-1] // current_number

                last_operator = char
                current_number = 0

        return sum(stack)
