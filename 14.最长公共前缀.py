#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.79%)
# Total Accepted:    50.4K
# Total Submissions: 158.5K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ''
        elif len(strs) == 1:
            return strs[0]

        meta = list(strs[0])
        comment_index = []
        for item in strs:
            single_match = 0
            # 开头不匹配，结束
            if not item or not meta or item[0] != meta[0]:
                comment_index = [0]
                break
            # 记录每个元素匹配的最大长度
            for i in range(len(meta)):
                if i <= len(item)-1 and item[i] == meta[i]:
                    single_match += 1
            comment_index.append(single_match)
        mutuel = min(comment_index)
        if mutuel == 0:
            comment = ''
        else:
            comment = ''.join([meta[i] for i in range(len(meta)) if i <= mutuel-1])
        return comment


if __name__ == '__main__':
    a = Solution()
    array = ["flower", "flow", "flight"]
    a.longestCommonPrefix(array)
