import pytest

from solution import Solution
S = Solution()

testCases = [
    ([2,1], False),
    ([1,2,3], False),
    ([3,2,1], False),
    ([1,2,3,2,1], True),
    ([1,2,3,2,3], False),
    ([2,3,2,1,0], True),
    ([1,3,2], True),
    ([3,5,5], False),
]

@pytest.mark.parametrize("input, expected", testCases)
def testSolution(input, expected):
    result = S.validMountainArray(input)
    assert result == expected
