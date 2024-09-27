from typing import List

class Solution(object):
    def run(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            opposite = target - num
            if opposite in seen:
                return [seen[opposite], index]
            seen[num] = index

        return None


inputs = [
    {
        "nums": [2,7,11,15],
        "target": 9
    },
    {
        "nums": [3,2,4],
        "target": 6
    },
    {
        "nums": [3,3],
        "target": 6
    }
]

solution = Solution()
results = []

for input in inputs:
    results.append(solution.run(**input))

print(results)
