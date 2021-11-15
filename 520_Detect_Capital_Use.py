# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-13 20:28:44
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-13 20:29:34
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.lower(), word[0].upper() + word[1:].lower())
