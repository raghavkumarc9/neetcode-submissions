class Solution:
    def hammingWeight(self, n: int) -> int:
        
        one_bit_counter = 0

        while n != 0:
            a = 0b001
            one_bit_counter += a & n
            n = n >> 1

        return one_bit_counter
