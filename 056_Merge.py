# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-18 00:27:30
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-18 00:28:23
from typing import List
from pysnooper import snoop


class Solution:
    @snoop()
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[i - 1][1]:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
