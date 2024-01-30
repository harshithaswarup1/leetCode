from collections import Counter

class Solution(object):
    def intersect(sellf,nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        
        # Iterate through the common elements in both counters
        common_elements = set(count1.keys()) & set(count2.keys())
        for num in common_elements:
            result.extend([num] * min(count1[num], count2[num]))
        
        return result
    
solution = Solution()
result = solution.intersect([4,9,5],[9,4,9,8,4])