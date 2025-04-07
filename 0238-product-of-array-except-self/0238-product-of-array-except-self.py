class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]* len(nums)
        postfix = [1]* len(nums)

        # prefix values [1, 1, 1, 1], num = [1,2,3,4]

        for i in range(1, len(nums)):
            prefix[i] =nums[i-1]* prefix[i-1] # pre = [1, 1, 2, 6]

        

        # postfix Vales [1, 1, 1, 1], num = [1, 2, 3, 4]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1] # post = [24,12,4,1]
        
        print(postfix)
        print(prefix)
            
        # storing the values 
        res =[]
        for i in range(0, len(nums)):
            res.append(prefix[i]*postfix[i])
        return res

        # nums = [1,2,3,4]
        # prefix = [1,1, 2, 6]
        # postfix = [24,12,4,1]
        # res = pre * post = [24,12,8,6]