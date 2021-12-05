# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-04 12:34:09
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-04 17:16:45
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_note,cnt_meg = Counter(ransomNote), Counter(magazine)
        return sum([1 if cnt_meg[k]>=v else 0 for k,v in cnt_note.items()])==len(cnt_note)


    # 更优雅
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        return not Counter(ransomNote) - Counter(magazine)

if __name__=='__main__':
    s = Solution()
    s.canConstruct('aa', 'aab')
    print(88872/200000)