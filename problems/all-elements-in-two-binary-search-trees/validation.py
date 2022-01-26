import pytest

from solution import Solution, TreeNode as T
S = Solution()

testCases = [
    (T(2,T(1),T(4)), T(1,T(0),T(3)), [0,1,1,2,3,4]),
    (T(1,T(8)), T(8,T(1)), [1,1,8,8]),
]

@pytest.mark.parametrize("input1, input2, expected", testCases)
def testSolution(input1, input2, expected):
    result = S.getAllElements(input1, input2)
    assert result == expected
