from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        counts = defaultdict(int)
        
        for char in s:
            counts[char] += 1
        
        for char in t:
            counts[char] -= 1
        
        for key in counts.keys():
            if counts[key] != 0:
                return False
   
        return True
    