# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-18 22:35:24
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-21 17:31:56
class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = bin(num)[2:]
        ans = ''.join(['0' if num == '1' else '1' for num in num_bin])
        return int(ans, base=2)


if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))

