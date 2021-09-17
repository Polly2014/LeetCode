# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-02 20:56:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-17 23:32:15
from typing import List


class Solution:

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

    # 更新子2021年9月17日，DP贪心
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 搞个图来存放最终结果集合
        graph = [[float('inf')] * n for _ in range(n)]
        # 用times信息更新到图上一波
        for src, dst, time in times:
            graph[src - 1][dst - 1] = time
        # 因为是求每个节点收到节点k的时间，因此只需要一个长度为n的数组存放距离即可，并将第k个节点的传播时间设置为0
        dist = [float('inf')] * n
        dist[k - 1] = 0
        # 再需要定义个访问数组，来记录哪些访问过
        used = [False] * n

        # 开始更新，总共n个节点，最多更新n次
        for _ in range(n):
            # 在未访问的节点中，寻找距离最近的
            idx = -1
            # 因为需要获得未使用的节点的下标，直接用enumerate枚举
            for i, use in enumerate(used):
                if not use and (idx == -1 or dist[idx] < dist[idx]):
                    idx = i
            used[idx] = True
            # 对找出的节点进行邻边遍历，更新一波dist数组
            for dst, time in enumerate(graph[idx]):
                dist[dst] = min(dist[dst], dist[x] + time)
        ans = max(dist)
        return ans if ans < float('inf') else -1

    # 更新子2021年9月17日，DFS
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass


if __name__ == '__main__':
    s = Solution()
    s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
