# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        a, b = 0, 0
        # Separate a, b into 2 groups..
        for num in nums:
            if num & -xor_sum & xor_sum: a ^= num
            else: b ^= num
        return [a,b]