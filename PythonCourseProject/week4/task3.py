"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=array&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
