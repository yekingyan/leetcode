#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
# 如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        # i 行， j 列
        # 同一左对角线的坐标(i, j), i1 - j1 == i2 - j2
        # 同一右对角线的坐标(i, j), i1 + j1 == i2 + j2
        def helper(left_diagonal, right_diagonal, column):
            if n == len(column):
                temp = []
                for line in board:
                    temp.append("".join(line))
                print(temp)
                res.append(temp)

            j = len(column)
            for i in range(n):
                if i in column:
                    continue
                if i - j in left_diagonal or i + j in right_diagonal:
                    continue
                board[j][i] = "Q"
                helper(left_diagonal + [i - j], right_diagonal + [i + j], column + [i])
                board[j][i] = "."

        helper(left_diagonal=[], right_diagonal=[], column=[])
        return res
# @lc code=end

