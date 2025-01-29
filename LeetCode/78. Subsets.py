class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        sol = []

        def bactrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            bactrack(i + 1)

            sol.append(nums[i])
            bactrack(i + 1)
            sol.pop()
        
        bactrack(0)
        return res