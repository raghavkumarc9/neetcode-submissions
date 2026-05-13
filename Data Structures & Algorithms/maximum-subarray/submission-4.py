class Solution:

    def maxSubArray(self, nums: List[int]) -> int:


        curr_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            if curr_sum >= 0 and nums[i] >= 0:
                curr_sum = curr_sum + nums[i]
                max_sum = curr_sum if curr_sum > max_sum else max_sum
            elif curr_sum >= 0 and nums[i] < 0: 
                curr_sum = curr_sum + nums[i]
                max_sum = curr_sum if curr_sum > max_sum else max_sum
            elif curr_sum < 0 and nums[i] >= 0:
                curr_sum = nums[i]
                max_sum = curr_sum if curr_sum > max_sum else max_sum
            else:
                curr_sum = nums[i]
                max_sum = curr_sum if curr_sum > max_sum else max_sum
        
        return max_sum