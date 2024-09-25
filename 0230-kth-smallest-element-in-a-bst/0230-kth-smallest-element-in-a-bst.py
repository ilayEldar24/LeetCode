# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    counter = 0
    number = -1
    def kthSmallest(self, root, k):
        def preOrder(root, k):
            if not root:
                return
            preOrder(root.left, k)
            self.counter += 1
            if self.counter == k:
                self.number = root.val
            preOrder(root.right, k)
        preOrder(root,k)
        return self.number
    
            
            
        