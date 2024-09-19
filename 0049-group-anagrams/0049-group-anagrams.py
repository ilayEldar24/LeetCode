from collections import defaultdict

def getCounts(str):
        lst = [0]*26
        
        for c in str:
            index = ord(c) - ord('a')
            lst[index] += 1
        
        return tuple(lst)

class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        
        for string in strs:
            codedString = getCounts(string)
            res[codedString].append(string)
        
        return res.values()
    


sol = Solution()

print(sol.groupAnagrams(
["eat","tea","tan","ate","nat","bat"]))
            

