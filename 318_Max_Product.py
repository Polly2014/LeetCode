# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-17 22:01:23
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-17 23:44:41
from typing import List
from functools import reduce
from itertools import product


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        m = {}
        for i in range(n):
            mask = 0
            for j in range(len(words[i])):
                mask |= 1 << ord(words[i][j]) - ord('a')
            m[i] = mask

        def intersected(i, j):
            # return set(words[i]).intersection(set(words[j]))
            return m[i] & m[j] != 0

        for i in range(n):
            for j in range(i + 1, n):
                if not intersected(i, j):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans

    def maxProduct(self, words: List[str]) -> int:
        masks = [reduce(lambda a, b: a | (1 << (ord(b) - ord('a'))), word, 0) for word in words]
        print(masks)
        return max((len(x[1]) * len(y[1]) for x, y in product(zip(masks, words), repeat=2) if x[0] & y[0] == 0), default=0)


if __name__ == '__main__':
    s = Solution()
    s.maxProduct(['abc', 'bcd', 'efgh'])
