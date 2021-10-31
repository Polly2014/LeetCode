# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-30 12:51:49
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-30 13:07:25
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        ans = [0, 0]
        for num in nums:
            xor ^= num
        flag = 1
        while (flag & xor == 0):
            flag <<= 1
        for num in nums:
            if flag & num == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))
