# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-30 22:21:42
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-30 22:51:27
from typing import List


class Solution:
        # 回溯
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     ans = []

    #     def BackTracking(new_list):
    #         if len(new_list) == n:
    #             ans.append(new_list[:])
    #             return
    #         for num in nums:
    #             if num not in new_list:
    #                 new_list.append(num)
    #                 BackTracking(new_list)
    #                 new_list.pop()
    #     BackTracking([])
    #     return ans

    # DFS
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def DFS(new_list):
            if len(new_list) == n:
                ans.append(new_list[:])
                return
            for num in nums:
                if num not in new_list:
                    DFS(new_list + [num])
        DFS([])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
