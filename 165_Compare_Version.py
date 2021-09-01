# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-01 10:14:33
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-01 10:48:54
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        m, n = len(v1), len(v2)
        if m > n:
            v2 += ['0'] * (m - n)
        else:
            v1 += ['0'] * (n - m)
        v = list(zip(map(int, v1), map(int, v2)))
        ans = 0
        for x, y in v:
            if x > y:
                ans = 1
                break
            elif x < y:
                ans = -1
                break
        return ans

    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        m, n = len(v1), len(v2)
        if m > n:
            v2 += ['0'] * (m - n)
        else:
            v1 += ['0'] * (n - m)
        v = list(zip(map(int, v1), map(int, v2)))
        for x, y in v:
            if x != y:
                return 1 if x > y else -1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion('7.5.2.4', '7.5.3'))
