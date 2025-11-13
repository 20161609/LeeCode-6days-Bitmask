# https://leetcode.com/problems/reverse-bits/description/?utm_source=chatgpt.com

class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(31):
            answer += (n%2)
            answer *= 2
            n//=2
        return answer