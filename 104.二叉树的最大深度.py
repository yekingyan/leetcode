#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 根点节就算一层

#  说明: 叶子节点是指没有子节点的节点。

# 示例：最大深度 3
# 给定二叉树 [3,9,20,null,null,15,7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepth1(root)

    @staticmethod
    def maxDepth1(rootNode):
        if rootNode is None:
            return 0
        que = collections.deque()
        que.append(rootNode)
        depth = 0
        while que:
            depth += 1
            for _ in range(len(que)):
                node = que.popleft()
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return depth
    
    @staticmethod
    def maxDepth2(rootNode):
        def _dfs(node, d):
            if node is None:
                return 0
            nonlocal depth
            if depth < d + 1:
                depth = d + 1
            _dfs(node.left, d + 1)
            _dfs(node.right, d - 1)
    
        if rootNode is None:
            return 0
        depth = 0
        _dfs(rootNode, 0)
        return depth
# @lc code=end