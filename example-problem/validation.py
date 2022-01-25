import pytest

from solution import Solution
S = Solution()

testCases = [
    ("fizz", "buzz"),
]

@pytest.mark.parametrize("input, expected", testCases)
def testSolution(input, expected):
    result = S.problemFunctionName(input)
    assert result == expected
