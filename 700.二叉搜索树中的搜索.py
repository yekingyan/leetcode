#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# 给定二叉搜索树:
# 
#         4
#        / \
#       2   7
#      / \
#     1   3
# 
# 和值: 2
# 你应该返回如下子树:
# 
#       2     
#      / \   
#     1   3

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.searchBST1(root, val)

    @classmethod
    def searchBST1(cls, root, val):
        if root is None or root.val == val:
            return root
        node = root.right if val > root.val else root.left
        return cls.searchBST1(node, val)

    @staticmethod
    def searchBST2(root, val):
        while True:
            if root is None or root.val == val:
                return root
            root = root.right if val > root.val else root.left

# @lc code=end

