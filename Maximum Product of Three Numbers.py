class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        num=sorted(nums)
        prod1=num[-1]*num[-2]*num[-3]
        prod2=num[0]*num[1]*num[-1]
        return max(prod1, prod2)
