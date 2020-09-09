#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树, 镜像对称
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetric1(root)

    @staticmethod
    def isSymmetric1(root):
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None \
                    or node2 is None \
                    or node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)

    @staticmethod
    def isSymmetric2(root):
        """层序遍历，然后检查每一层是不是回文数组"""
        ls = [root]
        while len(ls) > 0:
            next_ls = []
            layer = []
            for node in ls:
                if node is None:
                    layer.append(None)
                    continue
                next_ls.extend([node.left, node.right])
                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            ls = next_ls
        return True
# @lc code=end

