class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = [1] * len(nums)
#         left = [1] * len(nums)
#         right = [1] * len(nums)

#         for i in range(1, len(left)):
#             left[i] = left[i - 1] * nums[i - 1]

#         for i in range(len(right) - 2, -1, -1):
#             right[i] = right[i + 1] * nums[i + 1]

#         for i in range(len(nums)):
#             result[i] = left[i] * right[i]
        
#         return result
        