class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            temp = current_max
            current_max = max(num, num * current_max, num * current_min)
            current_min = min(num, num * temp, num * current_min)
            max_product = max(max_product, current_max)
        return max_product
    


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n==0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(temp, n*curMin, n) 
            res = max(res, curMax)
        return res