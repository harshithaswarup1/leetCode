class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if int(nums.count(num)) == 1:
                return num
                
solution = Solution()
result = solution.singleNumber([0,1,0,1,0,1,99])