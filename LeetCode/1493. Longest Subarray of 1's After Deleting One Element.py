class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, j = 0, 0
        k = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                k+=1

            while k >1:
                if nums[j]== 0:
                    k-=1
                j+=1
            max_count = max(max_count, i-j)
        return max_count
        