class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth=[]
        wealth_sum = 0
        for x in accounts:
            for x1 in x:
                wealth_sum += x1
            max_wealth.append(wealth_sum)
            wealth_sum = 0
        max_wealth = max(max_wealth)
        return max_wealth
            
solution = Solution()
result = solution.maximumWealth([[1,2,3],[3,2,1]])