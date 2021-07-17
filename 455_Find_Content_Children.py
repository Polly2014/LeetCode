# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-17 18:17:34
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-17 18:36:23
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        # 饼干
        idx = len(s) - 1
        ans = 0
        # 遍历孩子
        for i in range(len(g) - 1, -1, -1):
            if idx >= 0 and s[idx] >= g[i]:
                ans += 1
                idx -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1]))
