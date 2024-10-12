class Solution(object):
    def subsets(self, nums):
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return  # Add this return statement to exit the function
            
            subset.append(nums[i])  # Include the current element in the subset
            dfs(i + 1)  # Recur to include the next element
            
            subset.pop()  # Backtrack and remove the current element
            dfs(i + 1)  # Recur without including the current element
        
        dfs(0)
        return res
