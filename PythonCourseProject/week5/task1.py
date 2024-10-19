"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=hash-table&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(s)
            else:
                anagrams[sorted_str] = [s]

        return list(anagrams.values())
