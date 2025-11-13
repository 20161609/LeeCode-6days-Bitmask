# https://leetcode.com/problems/single-number/description/?utm_source=chatgpt.com

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = sum(2**b*(sum((v+(1<<32))>>b&1 for v in nums)%2) for b in range(32))
        return a if a<=(1<<31) else a-(1<<32)