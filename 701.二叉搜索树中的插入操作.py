#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
# insert-into-a-binary-search-tree

# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。
# 返回插入后二叉搜索树的根节点。
# 保证原始二叉搜索树中不存在新值。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.insertIntoBST1(root, val)

    @staticmethod
    def insertIntoBST1(root, val):
        def helper(node):
            if node is None:
                return TreeNode(val)
            if val > node.val:
                node.right = helper(node.right)
            else:
                node.left = helper(node.left)
            return node
        return helper(root)

    @staticmethod
    def insertIntoBST2(root, val):
        if root is None:
            return TreeNode(val)

        node, parent = root, root
        while node:
            parent = node
            node = parent.left if val < parent.val else parent.right
        
        if val < parent.val:
            parent.left = TreeNode(val)
        elif val > parent.val:
            parent.right = TreeNode(val)

        return root
# @lc code=end

