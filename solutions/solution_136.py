# https://leetcode.com/problems/single-number/description/?utm_source=chatgpt.com

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums: answer^=num
        return answer