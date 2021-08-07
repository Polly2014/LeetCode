# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-07 20:39:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-07 22:13:31
from typing import List


class Solution:
    '''
    # DP不太能解这道题
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + 1 if grid[i][0] == 1 else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + 1 if grid[0][j] == 1 else 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    dp[i][j] = 1
                    if grid[i - 1][j] == 1 and grid[i][j - 1] == 1:
                        print('Row:{}, Col:{}'.format(i + 1, j + 1))
                        num_0 = len(''.join(map(str, grid[i][:j + 1])).split('0')[-1])
                        print(num_0)
                        dp[i][j] = max(dp[i][j], dp[i - 1][j] + num_0)
                    if grid[i - 1][j] == 1 and grid[i][j - 1] == 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
                    if grid[i - 1][j] == 0 and grid[i][j - 1] == 1:
                        dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
                    if grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return max(max(dp))
        return dp
    '''

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def DFS(grid, i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + DFS(grid, i - 1, j) + DFS(grid, i + 1, j) + DFS(grid, i, j - 1) + DFS(grid, i, j + 1)
            return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, DFS(grid, i, j))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
