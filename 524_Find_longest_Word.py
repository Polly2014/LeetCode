# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-14 18:58:46
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-14 19:16:53
from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    def isSubSquence(self, s, word):
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return True if j == len(word) else False

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for word in dictionary:
            if self.isSubSquence(s, word):
                return word
        return ''


if __name__ == '__main__':
    s = Solution()
    print(s.findLongestWord('abpcplea', ["ale", "apple", "monkey", "plea"]))
