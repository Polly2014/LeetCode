# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-20 00:15:15
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-20 00:32:01
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, mod = divmod(sum(nums), k)
        # 优化1
        if mod:
            return False
        nums.sort()
        # 优化2
        if nums[-1] > target:
            return False
        # 优化3
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        def DFS(groups) -> bool:
            if not nums:
                return True
            num = nums.pop()
            for i in range(k):
                groups[i] += num
                if groups[i] <= target:
                    if DFS(groups):
                        return True
                groups[i] -= num
            nums.append(num)
            return False
        return DFS([0] * k)


if __name__ == '__main__':
    s = Solution()
    print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
