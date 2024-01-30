class Solution(object):
    def twoSum(self,nums, target):
        num_dict = {}
    
        for i, num in enumerate(nums,start=1):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        return []  


solution = Solution()

result = solution.twoSum([2, 7, 11, 15], 9)
result = solution.twoSum([2,3,4], 6)
result = solution.twoSum([-1,0], -1)