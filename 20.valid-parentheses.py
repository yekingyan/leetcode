#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.31%)
# Total Accepted:    45.7K
# Total Submissions: 125.9K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            # ')': '(',
            '{': '}',
            # '}': '{',
            '[': ']',
            # ']': '[',
        }
        s_list = list(s)

        def _delete_inside(s_list: list, operation: bool=False):
            """
            :param s_list:
            :param operation: 是否有操作
            :return:
            """
            if len(s_list) == 0:
                return True
            elif len(s_list) and operation:
                return False
            inside = []
            for i, item in enumerate(s_list):
                if i+1 < len(s_list) and brackets.get(item) == s_list[i+1]:
                    inside.append(i)
            for i, n in enumerate(inside):
                p1 = s_list.pop(n-2*i)
                p2 = s_list.pop(n-2*i)
            if len(inside) == 0:
                operation = True
            return _delete_inside(s_list, operation)
        return _delete_inside(s_list)


if __name__ == '__main__':
    a = Solution()
    strs = '[{}{[]}]'
    b = a.isValid(strs)
    print(b)
