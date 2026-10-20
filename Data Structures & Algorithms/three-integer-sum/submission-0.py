class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_counts = {}
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1
        result_list=[]

        for index_i in range(0,len(nums)):
            for index_j in range(index_i+1,len(nums)):
                third_num=-(nums[index_i]+nums[index_j])
                num_counts[nums[index_i]] -= 1
                num_counts[nums[index_j]] -= 1
                if num_counts.get(third_num, 0) > 0:
                    temp=[]
                    temp.append(nums[index_i])
                    temp.append(nums[index_j])
                    temp.append(third_num)
                    temp=sorted(temp)
                    if temp not in result_list:
                        result_list.append(temp)
                num_counts[nums[index_i]] += 1
                num_counts[nums[index_j]] += 1
    
        return result_list
        