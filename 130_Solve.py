# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-04 20:31:04
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-04 22:08:06
from typing import List
from collections import deque


class Solution:
    # DFS
    # 时间复杂度 O(m*n)
    # 空间复杂度 O(m*n)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def DFS(row, col):
            if not 0 <= row < m or not 0 <= col < n or board[row][col] != 'O':
                return
            board[row][col] = 'A'
            for r, c in dirs:
                DFS(row + r, col + c)

        for row in range(m):
            DFS(row, 0)
            DFS(row, n - 1)
        for col in range(n):
            DFS(0, col)
            DFS(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'A':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

    # BFS

    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        Q = deque()

        for row in range(m):
            if board[row][0] == 'O':
                Q.append((row, 0))
                board[row][0] = 'A'
            if board[row][n - 1] == 'O':
                Q.append((row, n - 1))
                board[row][n - 1] = 'A'
        for col in range(n):
            if board[0][col] == 'O':
                Q.append((0, col))
                board[0][col] = 'A'
            if board[m - 1][col] == 'O':
                Q.append((m - 1, col))
                board[m - 1][col] = 'A'
        while Q:
            row, col = Q.popleft()
            for r, c in dirs:
                rr, cc = row + r, col + c
                if 0 <= rr < m and 0 <= cc < n and board[rr][cc] == 'O':
                    Q.append((rr, cc))
                    board[rr][cc] = 'A'
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'A':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

    # 并查集
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
            self.count = n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            rootx, rooty = self.find(x), self.find(y)
            if rootx != rooty:
                if self.rank[rootx] > self.rank[rooty]:
                    rootx, rooty = rooty, rootx
                self.parent[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[y] += 1
                self.count -= 1

    def solve(self, board: List[List[str]]) -> None:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        dummy = m * n
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                        union(row * n + col, dummy)
                    else:
                        for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[row + r][col + c] == 'O':
                                union((row + r) * n + col + c, row * n + col)
        print(f)
        for row in range(m):
            for col in range(n):
                if find(dummy) == find(row * n + col):
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'


if __name__ == '__main__':
    s = Solution()
    s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
