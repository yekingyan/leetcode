#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
# 给定一个二叉树，返回它的中序 遍历。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        def _traversal(node):
            if node.left is not None:
                _traversal(node.left)
            res.append(node.val)
            if node.right is not None:
                _traversal(node.right)
        _traversal(root)
        return res
# @lc code=end

