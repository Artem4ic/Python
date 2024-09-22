"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD
"""


class Solution(object):
    def reverseWords(self, s):
        res = []
        string = s.split()[::-1]
        for i in string:
            res.append(i)
        return " ".join(string)
