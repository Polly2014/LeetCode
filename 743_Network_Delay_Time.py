# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-02 20:56:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-02 23:32:25
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 邻接矩阵
        g = [[float('inf')] * n for _ in range(n)]
        for s, t, time in times:
            g[s - 1][t - 1] = time
        # 距离数组
        dist = [float('inf')] * n
        dist[k - 1] = 0

        # 标记数组
        finished = [False] * n

        # for _ in range(n):
        #     # 在所有点中，找到未被标记的距离最近的点
        #     t = -1

        #     for idx, status in enumerate(finished):
        #         if status == False and (idx == -1 or dist[idx] < dist[t]):
        #             t = idx
        print(g)
        print([idx for idx, status in enumerate(finished) if not status])
        t = min([idx for idx, status in enumerate(finished) if not status and idx != (k - 1)], key=lambda x: dist[x])
        print(dist)


if __name__ == '__main__':
    s = Solution()
    s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
