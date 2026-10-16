class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        surfix=[]
        resultlist=[]
        surfix=[1]*len(nums)#[1,1,1,1]
        prefix.append(1)
        
        for i in range(1,len(nums)):
            if i==1:
                prefix.append(nums[0])
            else:
                product=prefix[i-1]*nums[i-1]#[1,1],[1,1,2]
                prefix.append(product)

        for i in range(len(nums)-2,-1,-1):#i=2,i=1
            surfix[i]=surfix[i+1]*nums[i+1]#[1,1,6,1],[,24,6,1]

        for i in range(0,len(nums)):
            resultlist.append(prefix[i]*surfix[i])
        
        return resultlist
        




        