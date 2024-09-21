class Solution(object):
    def minEatingSpeed(self, piles, h):
        l , r = 1, max(piles)
        lastValid = r
        while l <= r:
            mid = (l+r)//2
            if isEnough(piles, mid, h):
                lastValid = mid
                r = mid -1
            else:
                l = mid + 1
        return lastValid
            

def isEnough(piles, ratio, h):
    time = 0

    for pile in piles:
        time += (pile // ratio)
        if pile % ratio != 0:
            time += 1
    
    if time <= h :
        return True
    return False
    