# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-02 20:56:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-03 00:12:19
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')

        # 邻接矩阵
        matrix = [[INF] * n for _ in range(n)]
        for s, t, time in times:
            matrix[s - 1][t - 1] = time

        # 距离数组
        dist_k = [INF] * n
        dist_k[k - 1] = 0

        # 标记数组
        visited = [False] * n

        for _ in range(n):
                #----- 每次寻找'未访问 & 距离起点最近'的结点
            min_dist, t1 = INF, -1
            for i in range(n):
                if visited[i] == False and dist_k[i] < min_dist:
                    min_dist, t1 = dist_k[i], i
            if t1 == -1:
                break
            visited[t1] = True

            for t2, time in enumerate(matrix[t1]):
                dist_k[t2] = min(dist_k[t2], dist_k[t1] + time)
        ans = max(dist_k)
        return ans if ans < INF else -1

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #------------------------ floyd算法 -------------------------#
        INF = 10 ** 9
        edge = [[INF for _ in range(n)] for _ in range(n)]
        for x, y, cost in times:
            x -= 1
            y -= 1
            edge[x][y] = cost

        for x in range(n):
            edge[x][x] = 0

        for mid in range(n):
            for x in range(n):
                for y in range(n):
                    edge[x][y] = min(edge[x][y], edge[x][mid] + edge[mid][y])

        #----- 最后一个结点收到的时间。是求max
        start = k - 1
        res = max(edge[start])
        return res if res != INF else -1


if __name__ == '__main__':
    s = Solution()
    s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
