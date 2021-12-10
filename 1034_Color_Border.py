# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-07 22:45:05
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-07 22:58:01
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        visited = set()

        def DFS(x, y):
            if x < 0 or y < 0 or x == m or y == n:
                return True
            if (x, y) in visited:
                return
            if grid[x][y] != grid[row][col]:
                return True
            visited.add((x, y))
            ans = False
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if DFS(x + dx, y + dy):
                    ans = True
            if ans:
                grid[x][y] = color
            return False
        DFS(row, col)
        return grid
