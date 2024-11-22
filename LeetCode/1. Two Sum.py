class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            remaining = target-nums[i]
            if remaining in hashmap:
                return hashmap[remaining], i
            hashmap[nums[i]] = i
