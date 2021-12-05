# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-05 21:15:40
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-05 21:16:25
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
    	return pow(a, int(''.join(map(str, b)), 1337)
