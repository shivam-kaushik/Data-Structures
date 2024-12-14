class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1


# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left = 0
#         zeros_count = 0
#         max_length = 0

#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zeros_count += 1
            
#             while zeros_count > k:
#                 if nums[left] == 0:
#                     zeros_count -= 1
#                 left += 1
            
#             max_length = max(max_length, right - left + 1)
#         return max_length