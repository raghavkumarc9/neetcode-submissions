class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bit_counter = 0
        while n:
            n &= (n-1)
            one_bit_counter += 1
        return one_bit_counter
