# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-13 20:28:44
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-15 20:31:26
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.lower(), word[0].upper() + word[1:].lower())


if __name__ == '__main__':
    print(41.82 * 1.1 + 5 + 44.75 / 4 + 3.836 / 5 + 1.23)
