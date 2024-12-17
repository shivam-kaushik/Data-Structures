class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = gain[0]
        max_count = max(0, temp)
        for i in range(1,len(gain)):
            temp += gain[i]
            max_count = max(max_count, temp)
        return max_count