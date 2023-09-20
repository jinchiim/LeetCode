class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if i == val:
                for j in range(nums.count(i)):
                    nums.remove(i)
        return len(nums)