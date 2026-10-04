class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for n in nums:
            check=target-n
            if check in nums:
                result.append(nums.index(n))
                result.append(nums.index(check))
                return result
            else:
                continue
        