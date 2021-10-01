# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-01 10:40:51
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-01 11:11:05
from typing import List


class Solution:
	def destCity(self, paths: List[List[str]]) -> str:
        mp = {}
        for path in paths:
            mp[path[0]] = path[1]
        return (set(mp.values()) - set(mp.keys())).pop()

    def destCity(self, paths: List[List[str]]) -> str:
        mp = dict(paths)
        return (set(mp.values()) - set(mp.keys())).pop()

    def destCity(self, paths: List[List[str]]) -> str:
        return (set((city:=list(zip(*paths)))[1]) - set(city[0])).pop()


if __name__ == '__main__':
    s = Solution()
    print(s.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
