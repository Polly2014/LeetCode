# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-17 00:11:56
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-17 00:17:59
from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        ans = [0] * 4
        B = [0] * N
        max_sum = matrix[0][0]
        r1 = c1 = 0

        for i in range(M):
            B = [0] * N
            for j in range(i, M):
                cur_sum = 0
                for k in range(N):
                    B[k] += matrix[j][k]
                    if cur_sum > 0:
                        cur_sum += B[k]
                    else:
                        cur_sum = B[k]
                        r1, c1 = i, k
                    if cur_sum > max_sum:
                        max_sum = cur_sum
                        ans = [r1, c2, j, k]
        return ans
