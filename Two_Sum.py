class Solution(object):
    def twoSum(self,nums, target):
        num_dict = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            
            num_dict[num] = i
        return []  


solution = Solution()

result = solution.twoSum([2, 7, 11, 15], 9)
result = solution.twoSum([3,3], 6)