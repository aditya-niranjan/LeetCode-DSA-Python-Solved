# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def  solve(root):
            if root == None:
                return 0

            lefth  = solve(root.left)
            righth = solve(root.right)


            return 1 + max(lefth,righth)

        return solve(root)
