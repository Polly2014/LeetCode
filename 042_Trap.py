# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-31 15:00:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-31 23:49:06
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        ans = 0
        leftMax, rightMax = [0] * n, [0] * n
        leftMax[0], rightMax[0] = height[0], height[-1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i + 1])
        for i in range(n):
            ans += max(min(leftMax[i], rightMax[i]) - height[i], 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
