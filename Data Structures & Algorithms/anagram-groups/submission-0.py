class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)
        result=[]
        for num in strs:
             result_map[tuple(sorted(num))].append(num)
        return list(result_map.values())

                


       