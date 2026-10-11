class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return nums!=list(set(nums))
        return len(nums)!=len(set(nums))
        