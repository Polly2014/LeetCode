# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-21 22:22:21
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-21 23:11:12
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 两遍DFS
        # - 第一遍遍历陆地格子，计算每个岛屿的面积并标记岛屿
        # - 第二遍遍历海洋格子，观察每个海洋格子相邻的陆地格子
        m,n = len(grid), len(grid[0])
        area = {}
        index = 2

        # 计算对应编号的岛屿面积
        def DFS(grid, i, j, index):
            if 0<=i<m and 0<=j<n and grid[i][j]==1:
                grid[i][j] = index
                return 1+DFS(grid,i+1,j,index)+DFS(grid,i-1,j,index)+DFS(grid, i, j-1,index)+DFS(grid,i,j+1,index)
            return 0

        # 遍历，收集并更新岛屿编号及面积
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area[index] = DFS(grid, i, j,index)
                    index +=1
        print('-'*30)
        for g in grid:
            print(g)
        print('-'*30)
        print(area)

        def neighbors(i,j):
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=x<m and 0<=y<n:
                    yield x,y
                    
        # 遍历，尝试将海洋变为陆地，更新最大面积
        ans = max(area.values() or [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    seen = {grid[x][y] for x,y in neighbors(i,j) if grid[x][y]>1}
                    ans = max(ans, 1+sum(area[s] for s in seen))
        return ans

if __name__=='__main__':
    s = Solution()
    print(s.largestIsland([[1, 0], [0, 1]]))
