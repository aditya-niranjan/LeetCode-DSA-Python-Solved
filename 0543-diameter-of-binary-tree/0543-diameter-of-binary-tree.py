# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.dim = 0
        def fun(node):
            if node ==None:
                return 0
            lh = fun(node.left)
            rh = fun(node.right)
            self.dim = max(self.dim,lh+rh)
            
            return 1+ max(lh,rh)


        fun(root)

        return self.dim