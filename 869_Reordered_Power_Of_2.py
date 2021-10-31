# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-28 22:49:14
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-28 22:50:17
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        for i in range(32):
            if Counter(str(n)) == Counter(str(pow(2, i))):
                return True
        return False
