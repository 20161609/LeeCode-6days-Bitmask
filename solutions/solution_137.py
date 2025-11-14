# https://leetcode.com/problems/single-number-ii/?utm_source=chatgpt.com

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for b in range(32):
            remainder = sum((num+2**31)>>b & 1 for num in nums) % 3
            result += remainder*2**b
        print(result )
        return result - 2**31