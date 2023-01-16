class Solution:

    def getNextGreater(self, index: int, nums: List[int]):
        maxNum = nums[index]
        for i in range(index, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                return maxNum
        return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        maxs = []
        num2Len = len(nums2)
        for num in nums1:
            idx = nums2.index(num)
            maxs.append(self.getNextGreater(idx,nums2))
        return maxs


