# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-23 19:26:32
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-23 19:59:33
from typing import List
from collections import defaultdict
from queue import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 申请变量，存储邻接表
        dict_adj = defaultdict(set)
        # 更新临接表
        for u, v in edges:
            dict_adj[u].add(v)
            dict_adj[v].add(u)
        # 申请变量，用作队列，并将度为1的节点加入队列
        Q = deque([u for u, v in dict_adj.items() if len(v) == 1])
        # 存放结果
        ans = None
        # 开始循环遍历队列，将度维1的节点移除，并更新节点的度，同时将更新后度为1的节点加入队列
        while Q:
            ans = Q.copy()
            for _ in range(len(Q)):
                u = Q.popleft()
                for v in dict_adj[u]:
                    dict_adj[v].remove(u)
                    if len(dict_adj[v]) == 1:
                        Q.append(v)
                dict_adj.pop(u)
        return list(ans)
        # print(dict_adj)


if __name__ == '__main__':
    s = Solution()
    s.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])

# u->v
