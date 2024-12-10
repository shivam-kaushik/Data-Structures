class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] !=0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1

# i=j = 0 

# while j < len(nums):
#     if nums[i] == 0:
#         nums.append(nums[i])
#         nums.pop(i)
#     else:
#         i+=1
#     j+=1

