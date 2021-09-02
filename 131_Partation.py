# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-02 22:12:21
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-02 22:49:32
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        def BackTracking(path, idx):
            print('当前Path: {}, idx={}'.format(path, idx))
            if idx == n:
                print('得到可行解path:{}，返回'.format(path))
                ans.append(path[:])
                return
            for i in range(idx, n):
                seg = s[idx:i + 1]
                print('i={}, seg={}'.format(i, seg))
                if seg == seg[::-1]:
                    path.append(seg)
                    print('\t 回文,加入path中, path={}'.format(path))
                    BackTracking(path, i + 1)
                    path.pop()
                    print('\t 回溯，退栈, path={}'.format(path))
                else:
                    print('\t 非回文seg={}, 继续..'.format(seg))

        BackTracking([], 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.partition('aabc')
