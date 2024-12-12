class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_average = float('-inf')
        current_sum = sum(nums[:k])
        
        for i in range(n - k):
            max_average = max(max_average, current_sum / k)
            current_sum = current_sum - nums[i] + nums[i + k]
        
        return max(max_average, current_sum / k)