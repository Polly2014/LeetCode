# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-25 00:23:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-25 00:30:11
from typing import List
class Solution:
    # 暴力解法
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for element in row:
                if element==target:
                    return True
        return False

    # 逐行二分
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass


    # Z形二分
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        x,y = 0, n-1
        while x<m and y>=0:
            if matrix[x][y]==target:
                return True
            if matrix[x][y]>target:
                y-=1
            else:
                x+=1
        return False

