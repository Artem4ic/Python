"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/?envType=problem-list-v2&envId=sliding-window&status=TO_DO&difficulty=MEDIUM
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        closest_index = left

        left = closest_index - 1
        right = closest_index

        result = []

        for _ in range(k):
            if left < 0:
                result.append(arr[right])
                right += 1
            elif right >= len(arr):
                result.append(arr[left])
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1

        return sorted(result)
