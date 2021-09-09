# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-07 22:00:11
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-07 22:02:03
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        cnt = 0
        ans = 0
        for ss in s:
            if ss == 'L':
                cnt += 1
            elif ss == 'R':
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.balancedStringSplit('RLRRLLRLRL'))
