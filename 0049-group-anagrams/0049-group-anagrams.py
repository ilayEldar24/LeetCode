def getCounts(str):
        lst = [0]*26
        
        for c in str:
            index = ord(c) - ord('a')
            lst[index] += 1
        
        return tuple(lst)

class Solution(object):
    def groupAnagrams(self, strs):
        hmap = {}
        
        for string in strs:
            codedString = getCounts(string)
            if not hmap.get(codedString, 0):
                 hmap[codedString] = [string]
            else:
                 hmap[codedString].append(string)
        
        return hmap.values()
    
