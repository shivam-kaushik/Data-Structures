class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return result



# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()  
#         result = []

#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             target = -nums[i]
#             hashmap = {}
#             for j in range(i + 1, len(nums)):
#                 remaining = target - nums[j]
#                 if remaining in hashmap:
#                     triplet = [nums[i], nums[j], remaining]
#                     triplet.sort()
#                     if triplet not in result:
#                         result.append(triplet)
#                 hashmap[nums[j]] = j

#         return result
