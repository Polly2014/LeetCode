# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-21 23:28:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-22 12:41:00
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt = 0
                    for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if x<0 or x>=m or y<0 or y>=n or grid[x][y]==0:
                            cnt+=1
                    ans +=cnt
        return ans