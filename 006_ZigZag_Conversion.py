# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-19 14:26:37
# @Last Modified by:   polly
# @Last Modified time: 2021-06-19 15:25:17

# N型字符串

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ['' for _ in range(numRows)]
        start, n = 0, len(s)
        if n == 1:
            return s
        while start <= n:
            try:
                for i in range(numRows):
                    ans[i] += s[start]
                    start += 1
                for j in range(numRows - 2):
                    ans[numRows - j - 2] += s[start]
                    start += 1
            except:
                break
        return ''.join(ans)

# 更巧妙的解法是每numRows-1个数字看作一组，那么奇偶行变换方向，一切迎刃而解


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
