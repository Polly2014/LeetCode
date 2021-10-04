# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-02 22:43:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-02 23:03:16
class Solution:
    def toHex(self, num: int) -> str:
        MP = '0123456789abcdef'
        ans = []
        for _ in range(8):
            ans.append(num % 16)
            num //= 16
            if not num:
                break
        return ''.join(MP[i] for i in ans[::-1])
