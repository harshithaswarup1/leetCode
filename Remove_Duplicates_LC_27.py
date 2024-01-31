class Solution(object):
    import copy
    def removeElement(self, nums, val):
        new_list = copy.deepcopy(nums)#nums#.copy()
        for ele in new_list:
            if val in nums:
                nums.remove(val)
        out = len(nums)
        nums.extend(new_list.count(val)* "_")
        return out
    # .extend(new_list.count(val)* "_")
solution = Solution()
result = solution.removeElement([0,1,2,2,3,0,4,2],2)