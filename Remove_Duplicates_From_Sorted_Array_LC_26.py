
class Solution(object):
    def removeDuplicates(self, nums):
        unique_elements = list(set(nums))
        len_unique_elements = len(unique_elements)
        diff = len(nums) - len(unique_elements)
        unique_elements.extend(diff  * '_')
        print (list(set(nums)))


solution = Solution()
result = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])


# 80

class Solution(object):
    def removeDuplicates(self, nums):
        new_list = []
        for i in nums:
            if nums.count(i) <= 2:
                new_list.append(i)
        diff = list(set(nums) - set(new_list))
        new_list.extend(diff *2)
        new_list.sort()
        sorted_new_list = len(new_list)
        return sorted_new_list
        
solution = Solution()
result = solution.removeDuplicates([0,0,1,1,1,1,2,3,3])
        
        