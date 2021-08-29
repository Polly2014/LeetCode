# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-29 21:41:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-29 21:46:52
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        ans = 0
        while l <= r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
