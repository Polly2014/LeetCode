# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-29 22:32:25
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-29 22:39:24
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def cmp(x,y):
            return -1 if x[0]*y[1]<x[1]*y[0] else 1
        frac = []
        for i in range(n:=len(arr)):
            for j in range(i+1,n):
                frac.append((arr[i], arr[j]))
        frac.sort(key = cmp_to_key(cmp))
        return list(frac[k-1])
