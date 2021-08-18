# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-29 23:34:27
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-16 20:05:07
from typing import List


class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     heights = [0] + heights + [0]
    #     n, ans = len(heights), 0
    #     min_left_idx = [0] * n
    #     min_right_idx = [0] * n
    #     for i in range(1, n - 1):
    #         j = i - 1
    #         while j > 0 and heights[j] >= heights[i]:
    #             j -= 1
    #         min_left_idx[i] = j
    #     for i in range(n - 2, 0, -1):
    #         j = i + 1
    #         while j < n and heights[j] >= heights[i]:
    #             j += 1
    #         min_right_idx[i] = j
    #     for p in range(1, n - 1):
    #         print('w_r:{}, w_r:{}, h:{}'.format(min_right_idx[p], min_left_idx[p], heights[p]))
    #         ans = max(ans, (min_right_idx[p] - min_left_idx[p] - 1) * heights[p])
    #     return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        min_left_idx = [0] * n
        min_right_idx = [0] * n
        min_left_idx[0] = -1
        for i in range(1, n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j = min_left_idx[j]
            min_left_idx[i] = j
        min_right_idx[n - 1] = n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and heights[j] >= heights[i]:
                j = min_right_idx[j]
            min_right_idx[i] = j
        ans = 0
        for p in range(n):
            ans = max(ans, heights[p] * (min_right_idx[p] - min_left_idx[p] - 1))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([3, 1, 5, 6, 3, 2]))
