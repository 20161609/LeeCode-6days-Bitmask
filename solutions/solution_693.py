# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 1 if n%2==0 else 0
        while n:
            if prev^(n%2):
                n//=2
                prev ^= 1
            else:
                return False
        return True    