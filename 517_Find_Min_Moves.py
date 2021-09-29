# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-29 20:35:34
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-29 23:20:06
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        cnt_total = sum(machines)
        if cnt_total % n != 0:
            return -1
        cnt_avg = cnt_total // n
        ans = 0
        for i in range(n):
            ans = max(ans, abs(sum(machines[:i]) - i * cnt_avg), machines[i] - cnt_avg)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMinMoves([9, 1, 8, 8, 9]))
