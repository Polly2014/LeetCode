# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-15 12:37:47
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-16 22:35:54
from functools import lru_cache


class Solution:
    # def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    #     MOD = 1e9 + 7

    #     @lru_cache(None)
    #     def DFS(x, y, steps):
    #         if x < 0 or x >= m or y < 0 or y >= n:
    #             return 1
    #         if steps == 0:
    #             return 0
    #         return DFS(x + 1, y, steps - 1) % MOD + DFS(x - 1, y, steps - 1) % MOD + DFS(x, y + 1, steps - 1) % MOD + DFS(x, y - 1, steps - 1) % MOD
    #     return int(DFS(startRow, startColumn, maxMove) % MOD)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 1e9 + 7
        ans = 0

        def DFS(x, y, steps):
            if x < 0 or x >= m or y < 0 or y >= n:
                nonlocal ans
                ans += 1
                return
            if steps == 0:
                return
            DFS(x + 1, y, steps - 1)
            DFS(x - 1, y, steps - 1)
            DFS(x, y + 1, steps - 1)
            DFS(x, y - 1, steps - 1)
        DFS(startRow, startColumn, maxMove)
        return ans % MOD

    # def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
    #     mod = 10**9 + 7

    #     @lru_cache(None)
    #     def dp(x, y, remain):
    #         if remain < 0:
    #             return 0
    #         if x < 0 or x >= m or y < 0 or y >= n:
    #             return 1
    #         return dp(x + 1, y, remain - 1) % mod + dp(x - 1, y, remain - 1) % mod + dp(x, y + 1, remain - 1) % mod + dp(x, y - 1, remain - 1) % mod

    #     return dp(i, j, N) % mod


if __name__ == '__main__':
    s = Solution()
    print(s.findPaths(8, 7, 16, 1, 5))
