#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
# same-tree

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.isSameTree1(p, q)

    def isSameTree1(self, p, q):
        # 递归
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree1(p.left, q.left) and self.isSameTree1(p.right, q.right)

    def isSameTree2(self, p, q):
        # 队列
        ls = [p, q]
        while len(ls) > 0:
            node1 = ls.pop()
            node2 = ls.pop()
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            ls.extend([node1.left, node2.left, node1.right, node2.right])
        return True

# @lc code=end


