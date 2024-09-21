from collections import defaultdict

class TimeMap(object):

    def __init__(self):
        self.dic = defaultdict(list)
        
    def set(self, key, value, timestamp):
        self.dic[key].append([value,timestamp])

    def get(self, key, timestamp):
        lst = self.dic[key]

        l,r = 0, len(lst) - 1
        lastValid = ""
        
        while l <= r:
            mid = (l+r) // 2
            
            if lst[mid][1] <= timestamp:
                lastValid = lst[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return lastValid
