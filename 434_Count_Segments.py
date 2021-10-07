# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-07 00:17:51
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-07 00:18:49
class Solution:
    def countSegments(self, s: str) -> int:
        return len(list(filter(bool, s.split(' '))))


if __name__ == '__main__':
    s = Solution()
    p = '     '
    print(list(filter(bool, p.split(' '))))
