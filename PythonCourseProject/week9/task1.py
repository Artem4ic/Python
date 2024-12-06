"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees/?envType=problem-list-v2&envId=binary-tree&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
