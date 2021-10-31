# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-31 00:13:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-31 00:17:14
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(filter(lambda word: all(w in 'qwertyuiop' for w in word.lower()) or all(w in 'asdfghjkl' for w in word.lower()) or all(w in 'zxcvbnm' for w in word.lower()), words))
