class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        for num in set(nums):
            if nums.count(num)>=k:
                result.append(num)
            else:
                continue
        return result


        