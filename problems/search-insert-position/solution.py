from typing import List

class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            value = nums[mid]

            if value == target:
                return mid
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1

        return left + 1



"""
0, 5, 10, 15, 20, 25
L     M           R
10 != 22
10 < 22
L = M + 1

0, 5, 10, 15, 20, 25
          L   M   R
20 != 22
20 < 22
L = M + 1

0, 5, 10, 15, 20, 25
              L   R
              M
20 != 22
20 < 22
L = M + 1

L == R
return L + 1

"""



inputs = [
    {
        "nums": [1,3,5,6],
        "target": 5
    },
    {
        "nums": [1,3,5,6],
        "target": 2
    },
    {
        "nums": [1,3,5,6],
        "target": 7
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.searchInsert(**input))
