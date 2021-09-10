# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-09 22:39:52
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-10 00:26:23
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        # 第一步，将words分组，每一组对应结果中的一行
        line_list = []
        i, n = 0, len(words)
        while i < n:
            line = []
            line_length = 0
            while i < n and line_length + len(words[i]) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i]) + 1
                i += 1
            line_list.append(line)
        # 第二步，处理分组后的前n-1行，每行加入空格填充
        for i, line in enumerate(line_list[:-1]):
            if len(line) == 1:
                ans.append(line[0] + ' ' * (maxWidth - len(line[0])))
            else:
                num_words = len(line)
                length_words = sum(map(len, line))
                length_space = maxWidth - length_words
                avg_space = length_space // (num_words - 1)
                extra_sapce = length_space % (num_words - 1)
                left = (' ' * (avg_space + 1)).join(line[:extra_sapce + 1])
                mid = ' ' * avg_space if left else ''
                right = (' ' * avg_space).join(line[extra_sapce + 1:])
                ans.append(left + mid + right)
        #         print(length_words, avg_space, extra_sapce)
        # print(line_list)
        # print(ans)
        # 第三步，处理最后一行，加入空格填充
        text = ' '.join(line_list[-1])
        ans.append(text + ' ' * (maxWidth - len(text)))
        # 第三步 (写法二)
        # line = line_list[-1]
        # if len(line) == 1:
        #     ans.append(line[0] + ' ' * (maxWidth - len(line[0])))
        # else:
        #     text = ' '.join(line)
        #     ans.append(text + ' ' * (maxWidth - len(text)))
        # 第四部，合并最终结果
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    # ["This    is    an","example  of text","justification.  "]
    # ["This    is    an","example of text","justification.  "]
