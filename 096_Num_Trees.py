# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-23 23:29:11
# @Last Modified by:   polly
# @Last Modified time: 2021-06-24 00:00:10


class Solution:
    def numTrees(self, n: int) -> int:
        dp_nums = [0] * (n + 1)
        dp_nums[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp_nums[i] += (dp_nums[j - 1] * dp_nums[i - j])
        return dp_nums


if __name__ == '__main__':
    s = Solution()
    print(s.numTrees(2))
