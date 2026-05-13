class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        ## brute force
        """
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            output.append(product)

        return output
        """

        ## compute the product and divide by the i
        product = 1
        zero_counter = 0
        for i in nums:
            if i == 0:
                zero_counter += 1
            else:
                product *= i
        
        if zero_counter >= 2:
            return [0] * len(nums)
        one_zero = False
        if zero_counter == 1:
            one_zero = True

        for i in nums:
            if one_zero == True  and i != 0:
                output.append(0)
            elif one_zero == True and i == 0:
                output.append(product)
            else:
                output.append(product // i)
        
        return output
