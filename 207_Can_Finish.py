# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-18 21:40:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-18 22:22:09
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        indeg = [0] * numCourses
        for v, u in prerequisites:
            edges[u].append(v)
            indeg[v] += 1
        cnt = 0
        Q = deque([v for v in range(numCourses) if indeg[v] == 0])
        while Q:
            cnt += 1
            u = Q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    Q.append(v)
        return cnt == numCourses


if __name__ == '__main__':
    s = Solution()
    s.canFinish(4, [[1, 0], [0, 3]])
