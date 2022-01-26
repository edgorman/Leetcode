# 1305. All Elements in Two Binary Search Trees

Difficulty: ```Medium```

Source: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

## Description

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:

```
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
```

Example 2:

```
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
```

Constraints:
```
The number of nodes in each tree is in the range [0, 5000].
-10^5 <= Node.val <= 10^5
```

## Explanation

__Overview:__

Despite being a medium difficulty this was quite the easy problem to solve. It simply required merging the trees into a single flattened list (ignoring ordering between/within each binary tree) and then using the default sort method to automatically sort the numbers in ascending order. I decided to use a non-recursive method to save on memory, and instead used an interative approach to merge the two trees.

__Complexity:__

The time complexity for merging the binary trees is O(n) and the time complexity for the sort depends on what method python uses by default. Overall this is likely a O(n log n) solution.

The space complexity is O(n) for merging the binary trees since we need to store every value before sorting, and the sorting space complexity again will depend on which method python uses. 