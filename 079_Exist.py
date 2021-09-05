# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-02 23:47:30
# @Last Modified by:   polly
# @Last Modified time: 2021-09-05 15:34:11
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)

        def DFS(i, j, k):
            if k == n:
