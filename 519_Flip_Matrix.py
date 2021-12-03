# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-27 21:23:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-27 21:39:05
from typing import List
import random
class Solution:

    def __init__(self, m: int, n: int):
        self.m, self.n = m,n
        self.total = m*n-1
        self.record = {}


    def flip(self) -> List[int]:
        r = random.randint(0, self.total)
        idx = self.record.get(r,r)
        self.record[r] = self.record.get(self.total, self.total)
        self.total -=1
        ans = [idx//self.n, idx%self.n]
        return ans


    def reset(self) -> None:
        self.total = self.m*self.n-1
        self.record = {}



# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()