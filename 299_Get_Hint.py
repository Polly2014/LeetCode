# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-08 22:47:34
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-08 22:54:12
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        A_B = Counter(secret) & Counter(guess)
        A = sum(secret[i] == guess[i] for i in range(len(secret)))
        B = sum(A_B.values()) - A
        return '{}A{}B'.format(A, B)


if __name__ == '__main__':
    s = Solution()
    s.getHint('1807', '7817')
