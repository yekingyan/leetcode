#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
#    1.选出任一 x，满足 0 < x < N 且 N % x == 0 。
#    2.用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。
# 
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
# 数学归纳法，偶数出手胜

# @lc code=start
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:  # 抽到1输
            return False
        if N == 2:  # 抽到2赢
            return True

        target = [0 for _ in range(N + 1)]
        target[1] = 0
        target[2] = 1
        for i in range(3, N + 1):
            for j in range(1, i // 2):
                if i % j == 0 and target[i-j] == 0:
                    target[i] = 1
                    break
        return target[N] == 1
 # @lc code=end



