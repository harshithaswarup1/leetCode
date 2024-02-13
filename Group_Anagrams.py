class Solution(object):
    def groupAnagrams(self, strs):
        grouped_anagrams = {}
        for words in strs:
            sorted_word = "".join(sorted(words))
            if x in grouped_anagrams:
                grouped_anagrams[sorted_word].append(words)
            else:
                grouped_anagrams[sorted_word] = [words]
        return (list(grouped_anagrams.values()))
solution = Solution()
result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])



