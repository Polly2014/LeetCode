# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-05 17:35:59
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-05 19:21:03
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        hash_s, hash_t = defaultdict(int), defaultdict(int)
        for tt in t:
            hash_t[tt] += 1
        ans = ''
        left, right = 0, 0
        cnt = 0
        while right < len(s):
            sr = s[right]
            hash_s[sr] += 1
            if hash_s[sr] <= hash_t[sr]:
                cnt += 1
            while left <= right and hash_s[s[left]] > hash_t[s[left]]:
                hash_s[s[left]] -= 1
                left += 1
            if cnt == len(t):
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right + 1]
            print('Hash S: ', hash_s)
            print('Hash T: ', hash_t)
            print('-' * 20)
            right += 1

        return ans

    # def minWindow(self, s: str, t: str) -> str:
        '''
        如果hs哈希表中包含ht哈希表中的所有字符，并且对应的个数都不小于ht哈希表中各个字符的个数，那么说明当前的窗口是可行的，可行中的长度最短的滑动窗口就是答案。
        '''
        # if len(s) < len(t):
        #     return ""
        # hs, ht = defaultdict(int), defaultdict(int)  # 初始化新加入key的value为0
        # for char in t:
        #     ht[char] += 1
        # res = ""
        # left, right = 0, 0  # 滑动窗口
        # cnt = 0  # 当前窗口中满足ht的字符个数
        # while right < len(s):
        #     hs[s[right]] += 1
        #     if hs[s[right]] <= ht[s[right]]:  # 必须加入的元素
        #         cnt += 1  # 遇到了一个新的字符先加进了hs，所以相等的情况cnt也+1
        #     while left <= right and hs[s[left]] > ht[s[left]]:  # 窗口内元素都符合，开始压缩窗口
        #         hs[s[left]] -= 1
        #         left += 1
        #     if cnt == len(t):
        #         if not res or right - left + 1 < len(res):  # res为空或者遇到了更短的长度
        #             res = s[left:right + 1]
        #     right += 1
        #     print('Hash S: ', hs)
        #     print('Hash T: ', ht)
        #     print('-' * 20)
        # return res


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
