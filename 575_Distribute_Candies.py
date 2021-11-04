# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-01 19:54:07
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-02 10:29:17
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))


if __name__ == '__main__':
    print((77 * 3 + 87 * 2 + 85 * 2 + 78 * 1 + 88 * 1 + 78 * 1 + 86 * 3 + 86 * 3 + 69 * 2 + 82 * 1 + 77 * 3 +
           99 * 3 + 87 * 3 + 80 * 1 + 68 * 2) / (3 + 2 + 2 + 1 + 1 + 1 + 3 + 3 + 2 + 1 + 3 + 3 + 3 + 1 + 2))
