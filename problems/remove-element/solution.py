from typing import List

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 # position to insert numbers != val

        for right in range(0, len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left


"""
 2
[1,2,3]
   L
     R

left marks the last position where val was
right iterates through list and gives values to replace at index L
"""


inputs = [
    {
        "nums": [3,2,2,3],
        "val": 3
    },
    {
        "nums": [0,1,2,2,3,0,4,2],
        "val": 2
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.removeElement(**input))
