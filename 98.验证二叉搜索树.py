#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：
#     节点的左子树只包含小于当前节点的数。
#     节点的右子树只包含大于当前节点的数。
#     所有左子树和右子树自身必须也是二叉搜索树。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isBST1(root)

    def isBST1(self, root):
        def helper(node, minVal, maxVal):
            if node is None:
                return True
            if node.val >= maxVal or node.val <= minVal:
                return False
            return helper(node.left, minVal, node.val) \
                   and helper(node.right, node.val, maxVal)
        return helper(root, float("-inf"), float("inf"))

    def isBST2(self, root):
        """中序遍历"""
        def helper(node):
            if node is None:
                return
            helper(node.left)
            if node.val in res:
                nonlocal repeat
                repeat = True
                return
            res.append(node.val)
            helper(node.right)
        res = []
        repeat = False
        helper(root)
        if repeat:
            return False
        if res != sorted(res):
            return False
        return True
# @lc code=end

