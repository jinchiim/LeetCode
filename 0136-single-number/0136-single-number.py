class Solution(object):
    def singleNumber(self, nums):
         for i in set(nums):
            if nums.count(i) == 1:
                return i
        