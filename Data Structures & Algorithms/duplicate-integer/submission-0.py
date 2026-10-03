class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for n in nums:
            if n not in seen:
                seen.add(n)
        if len(seen)==len(nums):
            return False
        else:
            return True

        