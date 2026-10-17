class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_list=set(nums)
        max_count=0
        count=1
        for n in unique_list:
            if n-1 in unique_list:
                continue
            else:
                while n+1 in unique_list:
                    count+=1
                    n+=1
                max_count=max(max_count,count)
                count=1
        return max_count

                    







        