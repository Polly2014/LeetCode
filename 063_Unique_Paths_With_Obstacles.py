# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-23 00:16:25
# @Last Modified by:   polly
# @Last Modified time: 2021-06-23 00:16:32


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp_path = [[0] * n for _ in range(m)]
