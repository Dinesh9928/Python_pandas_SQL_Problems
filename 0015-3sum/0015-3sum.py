class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        nums.sort()
        # print(nums) [-10, -5, -5, -4, -4, -3, -2, -2, 0, 0, 1, 2, 2, 2, 2, 5, 5]
        n = len(nums)
        res = []
        # [-4,-4,-1,-1,0,1,2,2]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: # skiping duplicates 
                continue
            left = i+1
            right = n -1
            while(left < right):
                sum = nums[left] + nums[right] + nums[i]
                if sum < 0:
                    left +=1
                elif sum > 0:
                    right -=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left +=1
                    right -=1
        return res
                
        


        