class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] =prefix
            prefix *=nums[i] # res=[1,1,2,6], num = [1,2,3,4]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *=postfix
            postfix *= nums[i] #res =[24,12,8,6]]

        return res

       