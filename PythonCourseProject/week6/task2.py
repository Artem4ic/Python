"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []

        seen = set()
        duplicates = set()
        for i in range(len(s) - 9):
            seq = s[i : i + 10]
            if seq in seen:
                duplicates.add(seq)
            else:
                seen.add(seq)

        return list(duplicates)
