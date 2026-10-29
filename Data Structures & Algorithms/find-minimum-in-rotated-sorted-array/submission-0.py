class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp=0
        rp=len(nums)-1
        least=nums[0]

        while lp<=rp:
            mid=(lp+rp)//2

            if nums[lp]<=nums[mid]:
                least=min(least,nums[lp])
                lp=mid+1
            else:
                if nums[mid]<=nums[rp]:
                    least=min(least,nums[mid])
                    rp=mid-1
        return least
            
            


        