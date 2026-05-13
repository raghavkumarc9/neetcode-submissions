class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_dict = {}

        for i in range(len(nums)):
            if nums[i] not in store_dict.keys():
                store_dict[nums[i]] = i
            complement = target - nums[i]
            if complement in store_dict.keys() and store_dict[complement] != i:
                return [store_dict[complement], i]
          
