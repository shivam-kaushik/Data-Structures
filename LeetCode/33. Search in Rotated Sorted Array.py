class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                if target < nums[mid] and nums[start] <= target:
                    end = mid
                else:
                    start = mid
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid
                else:
                    end = mid
        
        return start if target == nums[start] else end if target == nums[end] else -1