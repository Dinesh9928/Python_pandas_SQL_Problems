class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
        if zero > 1:
            return [0]*len(nums)
        elif zero == 1:
            product = 1
            res = []
            for i in nums: 
                if i == 0:
                    continue
                else:
                    product = product * i
            for i in nums:
                if i == 0:
                    res.append(product)
                else:
                    res.append(0)
            return res
        else:
            product = 1
            res = []
            for i in nums: 
                    product = product * i
            for i in nums:
                    res.append(int(product/i))
            return res

        return [-1]




        