"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/word-subsets/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=MEDIUM
"""

from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        max_count = Counter()

        for word in words2:
            word_count = Counter(word)
            for char, freq in word_count.items():
                max_count[char] = max(max_count[char], freq)
        result = []

        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= freq for char, freq in max_count.items()):
                result.append(word)

        return result
