# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-23 22:00:20
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-23 22:14:58
from collections import Counter
from pysnooper import snoop
class Solution:
    @snoop()
    def buddyStrings(self, s: str, goal: str) -> bool:
        if not len(s)==len(goal):
            return False
        if not Counter(s)==Counter(goal):
            return False
        # 要么有恰好有两个不同，交换后相同
        # 要么不用交换两字符串即相同，同时字符串中包含重复字符
        if s==goal:
            return True if len(set(s))<len(gotal) else False
        num_diff = sum([0 if i==j else 1 for i,j in zip(s,goal)])
        if num_diff==0 or num_diff==2:
            return True
        return False

if __name__=='__main__':
    s = Solution()
    s.buddyStrings('abab', 'baab')

