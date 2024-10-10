# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        lst = []
        
        def helper(root, lst):
            if not root:
                return
            
            helper(root.left, lst)
            lst.append(root.val)
            helper(root.right, lst)
        
        helper(root, lst)
        return lst
        
            
                
                
        
        