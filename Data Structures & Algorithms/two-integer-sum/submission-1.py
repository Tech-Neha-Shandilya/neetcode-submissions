class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums):
            check=target-num
            if check in seen:
                return [seen[check],index]
            seen[num]=index
        return seen