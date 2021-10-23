# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-23 19:14:02
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-23 19:30:36
from typing import List
from collections import defaultdict, Counter


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.father = list(range(n))

    def find(self, i):
        if self.father[i] != i:
            self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        if rooti != rootj:
            if rooti > rootj:
                rooti, rootj = rootj, rooti
                i, j = j, i
            self.father[rootj] = rooti


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        # 建立可交换的并查集
        uf = UnionFind(n)
        for pair in allowedSwaps:
            uf.union(pair[0], pair[1])
        # 将每个下鼠标能匹配的集合统计出来
        allowedSet = defaultdict(dict)
        for i in range(n):
            if source[i] in allowedSet[uf.find(i)]:
                allowedSet[uf.find(i)][source[i]] += 1
            else:
                allowedSet[uf.find(i)][source[i]] = 1
        # 查找target每个元素是否能够匹配
        ans = 0
        for i in range(n):
            if target[i] not in allowedSet[uf.find(i)]:
                ans += 1
            # 将匹配的删除
            else:
                allowedSet[uf.find(i)][target[i]] -= 1
                if allowedSet[uf.find(i)][target[i]] == 0:
                    del allowedSet[uf.find(i)][target[i]]
        return ans


# ---------------------------------------------------------------- #
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = {i: i for i in range(n)}
        # 并查集

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        # 搜索根节点
        for pair in allowedSwaps:
            rootx, rooty = find(pair[0]), find(pair[1])
            if rootx != rooty:
                parent[rooty] = rootx
        # 获取根节点对应的连通块
        dic = collections.defaultdict(list)
        for i in range(n):
            rooti = find(i)
            dic[rooti].append(i)
        # 计算每个连通块对应的source元素与target的差集
        ans = 0
        for k, v in dic.items():
            x = [source[i] for i in v]
            cnt = Counter([target[i] for i in v])
            for xx in x:
                if cnt[xx] > 0:
                    cnt[xx] -= 1
                else:
                    ans += 1
        return ans
