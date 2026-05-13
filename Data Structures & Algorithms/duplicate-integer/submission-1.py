class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        original_len = len(nums)
        set_list = set()
        for i in range(len(nums)):
            set_list.add(nums[i])
        modified_len= len(set_list)
        if original_len==modified_len:
            return False
        else:
            return True