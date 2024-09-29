"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/remove-k-digits/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result else "0"
