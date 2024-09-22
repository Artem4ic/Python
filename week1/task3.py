"""
https://leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM%2CHARD
"""


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = [""]
        for i in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(i) - 50]:
                    queue.append((tmp + letter))
        return queue
