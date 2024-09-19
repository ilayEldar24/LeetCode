class Solution(object):
    def isValid(self, s):
        
        leftOrRight = {'(': 'Left', '{': 'Left', '[' : 'Left',
              ')': 'Right', '}': 'Right', ']' : 'Right'}
        
        stack = []
        
        
        for c in s:
            if leftOrRight[c] == 'Left':
                stack.append(c)
            else:
                if not stack:
                    return False
                lastLeft = stack.pop()
                if not isMatching(lastLeft, c):
                    return False
        
        if stack:
            return False
        
        return True

def isMatching(left, right):
    if (left == '(' and right == ')') or (left == '{' and right == '}') or (left == '[' and right == ']'):
        return True
    return False
                
sol = Solution()
sol.isValid('[({})]')               
        
        
        