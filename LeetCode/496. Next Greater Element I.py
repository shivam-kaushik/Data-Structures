class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dict = {}
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                popped = stack.pop()
                dict[popped] = nums2[i]
            stack.append(nums2[i])
            
        for i in range(len(nums1)):
            if nums1[i] in dict:
                nums1[i] = dict[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
