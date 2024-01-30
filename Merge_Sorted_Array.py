class Solution(object):
    def merge(self, nums1, m, nums2, n):
       number_list = nums1[:m] + nums2[:n]
       number_list.sort()
       for i in range(m + n):
           nums1[i] = number_list[i]
       print(nums1)
solution = Solution()
result = solution.merge([1,2,3,0,0,0],3,[2,5,6],3)