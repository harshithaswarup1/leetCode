class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}  
        for i, num in enumerate(nums):
            if num in num_indices and abs(i - num_indices[num]) <= k:
                return True
            num_indices[num] = i  
    
        return False

solution = Solution()
result = solution.containsNearbyDuplicate([1,2,3,1],3)