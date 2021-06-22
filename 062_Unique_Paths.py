# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-22 23:55:18
# @Last Modified by:   polly
# @Last Modified time: 2021-06-23 00:00:28


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_path = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                dp_path[row][col] = dp_path[row - 1][col] + dp_path[row][col - 1]
        return dp_path[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
