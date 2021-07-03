# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-03 17:13:43
# @Last Modified by:   Polly
# @Last Modified time: 2021-07-03 17:27:57
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(row)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
