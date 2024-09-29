"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1406265244/?envType=problem-list-v2&envId=string&difficulty=MEDIUM&status=TO_DO
"""


class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        max_count = 0
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[i]) - ord('A')])
            if (i - left + 1) - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

        return len(s) - left

#print(characterReplacement("ABAB", 2))
#print(characterReplacement("AABABBA", 1))
