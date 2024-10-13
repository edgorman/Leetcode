from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 1
        for left in range(1, len(nums)):
            if nums[left] != nums[left - 1]:
                nums[right] = nums[left]
                right += 1

        return right


inputs = [
    {
        "nums": [1, 1, 2]
    },
    {
        "nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.removeDuplicates(**input))
