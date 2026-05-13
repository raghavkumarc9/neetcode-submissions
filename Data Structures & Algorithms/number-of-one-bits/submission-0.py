class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bit_counter = 0

        while n != 0:
            one_bit_counter += n % 2
            n = n >> 1
        
        return one_bit_counter