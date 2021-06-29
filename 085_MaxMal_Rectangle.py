# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-28 23:59:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-29 00:00:26
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
