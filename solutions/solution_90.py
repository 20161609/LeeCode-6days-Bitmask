# https://leetcode.com/problems/subsets-ii/

from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.answer = []

        def backtrack(i, box):
            if len(nums) == i:
                self.answer.append(box[:])
                return
            if len(box)==0 or box[-1] != nums[i]:
                backtrack(i+1, box)
            box.append(nums[i])
            backtrack(i+1, box)
            box.pop()

        backtrack(0, [])
        return self.answer

