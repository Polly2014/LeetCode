# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-03 19:59:18
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-21 21:45:14
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

class UnionFind:
    def __init__(self, grid):
        m,n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1]*(m*n)
        self.rank = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    self.parent[i*n+j]=i*n+j
                    self.count+=1

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx!=rooty:
            if self.rank[x]<self.rank[y]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx]==self.rank[rooty]:
                self.rank[rootx]+=1
            self.count-=1

    def getCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    grid[i][j]='0'
                    for x,y in [(i-1,j),(i+1,j),(i,j-1), (i,j+1)]:
                        if 0<=x<m and 0<=y<n and grid[x][y]=='1':
                            uf.union(i*n+j,x*n+y)
        return uf.getCount()

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
