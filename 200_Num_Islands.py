# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-03 19:59:18
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-03 20:16:52
from typing import List


class Solution:
    def inArea(self, grid, i, j):
        return 0 <= i and i < len(grid) and 0 <= j and j < len(grid[0])

    def dfs(self, grid, i, j):
        if not self.inArea(grid, i, j):
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
