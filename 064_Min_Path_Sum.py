# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-21 23:41:33
# @Last Modified by:   polly
# @Last Modified time: 2021-06-22 00:02:16
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp_path = grid.copy()
        for row in range(1, rows):
            dp_path[row][0] = dp_path[row - 1][0] + grid[row][0]
        for col in range(1, cols):
            dp_path[0][col] = dp_path[0][col - 1] + grid[0][col]
        for row in range(1, rows):
            for col in range(1, cols):
                dp_path[row][col] = min(dp_path[row - 1][col], dp_path[row][col - 1]) + grid[row][col]
        return dp_path[rows - 1][cols - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
