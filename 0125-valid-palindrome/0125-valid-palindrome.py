def preProcess(s):
    lower = s.lower()
    return ''.join(char for char in lower if char.isalpha() or char.isnumeric())


class Solution(object):
    def isPalindrome(self, s):
        processed = preProcess(s)
        l = 0
        r = len(processed) - 1
        while l < r :
            if processed[l] != processed[r]:
                return False
            l+=1
            r-=1
        return True
