class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        result=[]
        for num in nums:
            hash_map[num]=hash_map.get(num, 0) + 1
        sorted_pairs = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        for count in range(0,k):
            result.append(sorted_pairs[count][0])
        return result

        


        