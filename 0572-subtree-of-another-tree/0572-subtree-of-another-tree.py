# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def SameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            else:
                return p.val==q.val and SameTree(p.left, q.left) and SameTree(p.right,q.right)
        
        if root and subRoot:
            if root.val == subRoot.val:
                if SameTree(root, subRoot):
                    return True
        if not subRoot:
            return True
        
        if not root:
            return False
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)