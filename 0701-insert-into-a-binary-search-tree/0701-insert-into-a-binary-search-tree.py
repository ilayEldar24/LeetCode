# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        def helper(root,val):  
            if val < root.val:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    helper(root.right, val)               
                else:
                    root.right = TreeNode(val)
        
        if not root:
            return TreeNode(val)
        else:
            helper(root,val)
            return root
