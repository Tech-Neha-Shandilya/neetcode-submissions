class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pre_area=0
        curr_area=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                length=min(heights[i],heights[j])
                curr_area=length*(j-i)
                curr_area=max(curr_area,pre_area)
                pre_area=curr_area
        return curr_area







        