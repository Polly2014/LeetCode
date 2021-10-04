# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-01 15:28:10
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-01 15:46:43
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = list(zip(*matrix))
        matrix = [sorted(m, reverse=True) for m in matrix]
        return matrix

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] =\
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
