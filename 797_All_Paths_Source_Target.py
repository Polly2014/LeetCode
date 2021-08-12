# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-12 22:32:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-12 22:50:33
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def DFS(node, path):
            if node == n - 1:
                print('Path: {}'.format(path))
                ans.append(path[:])
                return
            for i in graph[node]:
                path += [i]
                DFS(i, path)
                path.pop(-1)
        DFS(0, [0])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))
