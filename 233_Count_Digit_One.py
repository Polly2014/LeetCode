# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-05 23:34:10
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-15 10:56:38


class Solution:
    def countDigitOne(self, n: int) -> int:
    	'''
        ans = 0
        for i in range(1, n + 1):
            ans += str(i).count('1')
        return ans
        '''
        count, i = 0, 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i = divider


if __name__ == '__main__':
    s = Solution()
    print(s.countDigitOne(13))
