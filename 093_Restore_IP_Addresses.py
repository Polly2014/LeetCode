# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-14 23:32:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-20 19:06:07
from typing import List
from pysnooper import snoop


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        ans = []

        @snoop()
        def BackTracking(s, path, startIndex):
            if len(path) == 4:
                if startIndex == len(s):
                    ans.append('.'.join(path[:]))
                return
            # 剪枝，当前未处理字符长度>（待生产IP个数*3）
            if n - startIndex > (4 - len(path)) * 3:
                return
            # 单层循环逻辑
            for i in range(1, 4):
                if startIndex + i > n:
                    continue
                ip_str = s[startIndex:startIndex + i]
                if len(ip_str) > 1 and ip_str[0] == '0':
                    continue
                if int(ip_str) > 255:
                    continue
                path.append(ip_str)
                BackTracking(s, path, startIndex + i)
                path.pop()
        BackTracking(s, [], 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses('0000'))
