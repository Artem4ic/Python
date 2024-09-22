"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        maxLength = 0
        left = 0
        right = 0
        arr = [0] * 256

        while right < len(s):
            while arr[ord(s[right])]:
                arr[ord(s[left])] = 0
                left += 1

            arr[ord(s[right])] = 1
            maxLength = max(maxLength, right - left + 1)
            right += 1

        return maxLength


# s = input()
# print(Solution.lengthOfLongestSubstring((s)))
