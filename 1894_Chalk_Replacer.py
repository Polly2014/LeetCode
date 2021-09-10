# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-10 19:37:41
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-10 19:41:20
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        num_one_loop = sum(chalk)
        k = k % num_one_loop
        print(k)
        i = 0
        while k:
            if k >= chalk[i]:
                k -= chalk[i]
                i += 1
            else:
                break
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.chalkReplacer([3, 4, 1, 2], 25))
