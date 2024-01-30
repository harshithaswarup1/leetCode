class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        num_set = set(nums)
        disappeared_numbers = [i for i in range(1, n + 1) if i not in num_set]
        return disappeared_numbers
        
solution = Solution()
result = solution.findDisappearedNumbers([1,1,4])