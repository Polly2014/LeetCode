# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-07 22:44:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-07 23:02:31
from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # deque中的每个元素： <idx, mask, dist>
        # 状态值mask初始值，仅当前节点被访问，因此是 1<<i
        q = deque([(i, 1 << i, 0) for i in range(n)])
        visited = set([(i, 1 << i) for i in range(n)])

        while q:
            # 取出队首元素
            idx, mask, dist = q.popleft()
            # 根据状态值mask是否为2^n-1来判定是否遍历完毕
            if mask == (1 << n) - 1:
                return dist
            # 扩展（根据队首元素，加入与其相连的元素），该信息需要从graph[i]中获得
            for node in graph[idx]:
                # 或运算
                nextmask = mask | 1 << node
                if (node, nextmask) not in visited:
                    q.append((node, nextmask, dist + 1))
                    visited.add((node, nextmask))
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.shortestPathLength([[1, 2, 3], [0], [0], [0]]))
