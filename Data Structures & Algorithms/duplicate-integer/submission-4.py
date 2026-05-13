class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_copy = set(nums)
        if len(nums_copy) == len(nums):
            return False

        return True