# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = 0
        for b in range(32):
            cnt = 0
            for num in nums:
                num += 2**31
                cnt += (num>>b) & 1
            result += (cnt%2)*(2**b)
        print(result)
        print(result-(2**31))
        