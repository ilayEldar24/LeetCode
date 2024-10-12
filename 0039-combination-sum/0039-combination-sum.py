class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        curSet = []
        
        def dfs(i):
            if i >= len(candidates):
                if sum(curSet) == target:
                    res.append(curSet.copy())
                return
            
            if sum(curSet) > target:
                return
            
            curSet.append(candidates[i])
            dfs(i)
            
            curSet.pop()
            dfs(i+1)
        
        dfs(0)
        return res
    