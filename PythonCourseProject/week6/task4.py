"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter

        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        p_count = Counter(p)
        s_count = Counter()

        result = []

        for i in range(len_p):
            s_count[s[i]] += 1

        if s_count == p_count:
            result.append(0)

        for i in range(len_p, len_s):
            s_count[s[i]] += 1
            s_count[s[i - len_p]] -= 1

            if s_count[s[i - len_p]] == 0:
                del s_count[s[i - len_p]]

            if s_count == p_count:
                result.append(i - len_p + 1)

        return result
