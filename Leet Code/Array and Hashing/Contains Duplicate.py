class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()
        for num in nums:
            if num in distinct_nums:
                return True 
            distinct_nums.add(num)
        return False