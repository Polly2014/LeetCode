# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-14 21:26:29
# @Last Modified by:   polly
# @Last Modified time: 2021-11-14 22:58:37
'''
class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        return sum([v for k, v in self.map.items() if k.startswith(prefix)])
'''

'''
# DFS
class MapSum:

    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for k in key:
            if k not in node:
                node[k] = {}
            node = node[k]
        node['#'] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for k in prefix:
            if k not in node:
                return 0
            node = node[k]
        return self.DFS(node)

    def DFS(self, node):
        ans = 0
        for k in node:
            if k == '#':
                ans += node[k]
            else:
                ans += self.DFS(node[k])
        return ans
'''

'''
# BFS
class MapSum:

    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        node = self.trie
        for k in key:
            if k not in node:
                node[k] = {}
            node = node[k]
        node['#'] = val

    def sum(self, prefix: str) -> int:
        node = self.trie
        for k in prefix:
            if k not in node:
                return 0
            node = node[k]
        Q = [node]
        ans = 0
        while Q:
            node = Q.pop(0)
            for k, v in node.items():
                if k == '#':
                    ans += v
                else:
                    Q.append(v)
        return ans
'''
class MapSum:
    def __init__(self):
        self.map = {}
        self.prefixmap = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        for i in range(len(key)):
            currprefix = key[0:i+1]
            if currprefix in self.prefixmap:
                self.prefixmap[currprefix] += delta
            else:
                self.prefixmap[currprefix] = delta

    def sum(self, prefix: str) -> int:
        if prefix in self.prefixmap:
            return self.prefixmap[prefix]
        else:
            return 0
            
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
