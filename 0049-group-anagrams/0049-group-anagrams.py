class Solution(object):
    def groupAnagrams(self, strs):
        hmap = {}
        
        for string in strs:
            sotred_string = tuple(sorted(string))
            if not hmap.get(sotred_string, 0):
                hmap[sotred_string] = [string]
            else:
                hmap[sotred_string].append(string)
        
        return hmap.values()
            