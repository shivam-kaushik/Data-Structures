class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result



# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = Counter(nums)
        
#         for num, count in counts.items():
#             if count == 1:
#                 return num