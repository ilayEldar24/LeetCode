from collections import deque

class Solution(object):
    def levelOrder(self, root):
        queue = deque()

        if root:
            queue.append(root)

        curLevel = []
        res = []

        while queue:
            levelLen = len(queue)

            for i in range(levelLen):
                cur = queue.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            res.append(curLevel)
            curLevel = []
        
        return res




        
        