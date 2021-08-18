# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-16 22:40:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-16 23:39:48
from collections import defaultdict


class Solution:
        # 方法一：回溯
        # 回溯的时间复杂度 O(n!)，因为是遍历一颗树
        # match数组预处理时间复杂度 O(n^2)
        # match数组空间复杂度 O(n^2)，用于保存match数组
        # 递归栈的复杂度 O(n)
    def countArrangement(self, n: int) -> int:
        # match数组用于统计结果中每个位置上可以放置的数字
        match = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    match[i].append(j)
        # used用于存储在回溯过程中，已经使用过了的数字
        used = set()
        ans = 0

        def DFS(idx):
            if idx > n:
                nonlocal ans
                ans += 1
                return
            for v in match[idx]:
                if v not in used:
                    used.add(v)
                    DFS(idx + 1)
                    used.remove(v)
        DFS(1)
        return ans

    # 方法二：动态规划+状态压缩
    # 状态压缩一半就是用一位数组（如用位运算）

    def countArrangement(self, n: int) -> int:
    	# 用来存储中间结果，f[6] = f[000110] = 数字2、3在前两位时的完美排列数量
        dp = [0] * (1 << n)
        dp[0] = 1
        # mask表示了不同的排列方式（其中二进制下包含1的个数表示有多少位被占用，1所在的位置则表示了该位被用于排列）
        # 通过 mask 进行枚举，最终目的是为了得到二进制 mask = (11..11)n 时，总的完美排列数
        for mask in range(1, 1 << n):
            num = bin(mask).count('1')
            for i in range(n):
            	# mask & (1<<i) 用来判断 mask 第 i 位是否为 1，如果为 1，说明第 i+1 个数字被选取
            	# ((num % (i + 1)) == 0 || (i + 1) % num == 0) 判断被选取的数字 i+1 能否放到位置 num 上，
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                	# mask ^ (1 << i) 将 mask 第 i 位设置为 0
                    dp[mask] += dp[mask ^ (1 << i)]
        return dp[(1 << n) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.countArrangement(5))
