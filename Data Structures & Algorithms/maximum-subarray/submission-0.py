class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum
        
        return max_sum

        """
        if len(nums) == 1:
            return nums[0]

        curr_sum = None
        max_sum = 0

        # if curr_sum + i > 0

        for i in range(len(nums)):
            if curr_sum == None:
                curr_sum, max_sum = nums[i]
            elif curr_sum > 0 and nums[i] > 0:
                curr_sum = curr_sum + nums[i]
                max_sum = curr_sum
            elif curr_sum < 0 and nums[i] > 0: #we want to restart
                curr_sum = nums[i]
                max_sum = curr_sum
            elif curr_sum > 0 and nums[i] < 0:
                curr_sum = curr_sum + nums[i]
            else curr_sum < 0 and nums[i] < 0
        """


        




        