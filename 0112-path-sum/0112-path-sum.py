# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        #Case Empty Tree
        if not root:
            return False

        #Case leaf
        if not (root.left or root.right):
            return targetSum - root.val == 0
        
        
        if self.hasPathSum(root.left, targetSum - root.val):
            return True
        
        if self.hasPathSum(root.right, targetSum - root.val):
            return True
        
        return False

        

            
        