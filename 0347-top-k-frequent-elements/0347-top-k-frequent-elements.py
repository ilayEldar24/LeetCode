from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        
        sortedArray = sorted(nums)
        hmap = defaultdict(list)
        
        count = 0 
        for index, num in enumerate(sortedArray):
            count +=1
            if(index == len(sortedArray) -1):
                hmap[count].append(num)
            elif sortedArray[index+1] != num :
                hmap[count].append(num)
                count = 0
        
        sortedCounts = sorted(hmap.keys(), reverse=True)
        
        res = [] 
        
        for count in sortedCounts:
            
            while(hmap[count]):
                res.append(hmap[count].pop())
                k-=1
                if k==0:
                    return res

        
        