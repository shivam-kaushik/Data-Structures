class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        indexStack = []
        
        for i in range(len(nums)):
            if indexStack and indexStack[0] < i - k + 1:
                indexStack.pop(0)
            while indexStack and nums[indexStack[-1]] <= nums[i]:
                indexStack.pop()
            
            indexStack.append(i)
            if i >= k - 1:
                result.append(nums[indexStack[0]])
        
        return result
