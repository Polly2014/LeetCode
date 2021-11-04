# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-03 21:12:35
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-03 21:24:28
from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        visited = [[False] * n for _ in range(m)]
        ans = 0

        # 最外层放入队中
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # 上下左右四个方向
        dirs = (0, 1, 0, -1, 0)
        while heap:
            min_height, x, y = heapq.heappop(heap)
            for k in range(4):
                dx = dirs[k]
                dy = dirs[k + 1]
                xx, yy = x + dx, y + dy
                if 0 < xx < m - 1 and 0 < yy < n - 1 and not visited[xx][yy]:
                    if min_height > heightMap[xx][yy]:
                        ans += min_height - heightMap[xx][yy]
                    # 将xx,yy入堆
                    heapq.heappush(heap, (max(heightMap[xx][yy], min_height), xx, yy))
                    visited[xx][yy] = True
        return ans
