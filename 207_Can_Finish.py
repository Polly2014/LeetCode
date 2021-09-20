# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-18 21:40:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-18 23:42:25
from typing import List
from collections import defaultdict, deque


class Solution:
    # 经典BFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储边（节点依赖关系）
        edges = defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 更新边信息及节点度信息
        for v, u in prerequisites:
            edges[u].append(v)
            indeg[v] += 1
        # 用于记录结果中节点个数
        cnt = 0
        # 队列，初始化时即可将入读为0的节点放入队列中
        Q = deque([v for v in range(numCourses) if indeg[v] == 0])
        # 反复检查队列
        while Q:
            # 结果个数+1，弹出队列头元素
            cnt += 1
            u = Q.popleft()
            # 根据头节点，更新其关联节点的入度
            for v in edges[u]:
                indeg[v] -= 1
                # 更新完后，需要判断是否有节点度为0，有则加入队列中
                if indeg[v] == 0:
                    Q.append(v)
        return cnt == numCourses

    # 经典DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储边（节点依赖关系）
        edges = defaultdict(list)
        # 存储每个节点访问状态，0-未访问，1-访问中，2-已访问
        visited = [0] * numCourses
        # 存储结果
        ans = []
        # 标记是否异常（如遇到环），用于提前结束
        valid = True
        # 更新边信息及节点度信息
        for v, u in prerequisites:
            edges[u].append(v)

        def DFS(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                # 邻接节点未访问，可以继续搜索下去
                if visited[v] == 0:
                    DFS(v)
                    if not valid:
                        return
                # 邻接节点访问中，遇到环，将状态标记为异常
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            ans.append(u)
        for i in range(numCourses):
            if valid and not visited[i]:
                DFS(i)
        return valid


if __name__ == '__main__':
    s = Solution()
    s.canFinish(4, [[1, 0], [0, 3]])
