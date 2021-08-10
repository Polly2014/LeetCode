# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-09 23:21:58
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-10 00:32:28
from typing import List


class Solution:
    '''
    # 太骚了
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
    '''

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1
        ans = []
        while top <= bottom and left <= right:
            if top == bottom and left == right:
                ans += [matrix[top][left]]
                break
            elif top == bottom:
                ans += matrix[top][left:right + 1]
                break
            elif left == right:
                ans += [matrix[i][right] for i in range(top, bottom + 1)]
                break
            else:
                ans += matrix[top][left:right]
                ans += [matrix[i][right] for i in range(top, bottom)]
                ans += matrix[bottom][right:left:-1]
                ans += [matrix[i][left] for i in range(bottom, top, -1)]
                top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
            print(top, bottom, left, right)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]))
