# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-13 00:03:01
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-13 00:05:15
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            if not s:
                s += str(i)
            ans.append(s)
        return ans
