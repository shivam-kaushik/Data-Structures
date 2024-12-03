class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        tempLen = 1
        maxLen = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i-1]:
                tempLen +=1
            else:
                tempLen = 1

            if tempLen > maxLen:
                maxLen = tempLen
        return maxLen
