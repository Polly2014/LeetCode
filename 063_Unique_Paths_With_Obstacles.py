# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-23 00:16:25
# @Last Modified by:   polly
# @Last Modified time: 2021-06-23 12:04:50
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp_path = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            if obstacleGrid[row][0] == 0:
                dp_path[row][0] = 1
            else:
                break
        for col in range(cols):
            if obstacleGrid[0][col] == 0:
                dp_path[0][col] = 1
            else:
                break
        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 0:
                    dp_path[row][col] = dp_path[row - 1][col] + dp_path[row][col - 1]
                else:
                    dp_path[row][col] = 0
        return dp_path[rows - 1][cols - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
