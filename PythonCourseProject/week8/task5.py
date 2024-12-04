"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/fruit-into-baskets/submissions/1470466724/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        fruit_count = {}
        max_fruits = 0

        for right in range(len(fruits)):
            if fruits[right] in fruit_count:
                fruit_count[fruits[right]] += 1
            else:
                fruit_count[fruits[right]] = 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
