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