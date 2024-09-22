"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD
"""


class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                t1, t2 = i + j, i + j + 1
                mul += res[t2]
                res[t1] += mul // 10
                res[t2] = mul % 10

        arr = []
        for i in res:
            if len(arr) != 0 or i != 0:
                arr.append(str(i))

        return "".join(arr)
