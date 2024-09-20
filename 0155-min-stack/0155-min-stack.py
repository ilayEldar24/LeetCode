class MinStack(object):
    stack = []
    size = 0 
    

    def __init__(self):
        self.stack = []
        self.size =0
        
        

    def push(self, val):
        if self.size==0:
            self.stack.append([val,val])
        else:
            if val < self.stack[self.size-1][1]:
                self.stack.append([val,val])
            else:
                self.stack.append([val,self.stack[self.size-1][1]])
        self.size += 1
        
                
        
    def pop(self):
        lastItem = self.stack.pop()
        self.size-=1
        return lastItem[0]
        

    def top(self):
        return self.stack[self.size-1][0]
        

    def getMin(self):
        return self.stack[self.size-1][1]
        
