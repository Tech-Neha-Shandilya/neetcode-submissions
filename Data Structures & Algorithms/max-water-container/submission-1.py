class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pre_area=0
        curr_area=0
        lp=0
        rp=len(heights)-1
        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):
        #         length=min(heights[i],heights[j])
        #         curr_area=length*(j-i)
        #         curr_area=max(curr_area,pre_area)
        #         pre_area=curr_area
        # return curr_area
        while lp<rp:
            width=rp-lp
            length=min(heights[lp],heights[rp])
            curr_area=length*width
            curr_area=max(curr_area,pre_area)
            pre_area=curr_area
            if heights[lp]>heights[rp]:
                rp-=1
            else:
                lp+=1
        return curr_area











        