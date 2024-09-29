from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        max_index = min([len(str) for str in strs])

        while index < max_index and all([str[index] == strs[0][index] for str in strs]):
            index += 1

        return strs[0][0:index]


inputs = [
    {
        "strs": ["flower","flow","flight"]
    },
    {
        "strs": ["dog","racecar","car"]
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.longestCommonPrefix(**input))
