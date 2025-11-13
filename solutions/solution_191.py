# https://leetcode.com/problems/number-of-1-bits/description/?utm_source=chatgpt.com

class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()