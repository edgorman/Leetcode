from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"<value={self.val};next={self.next}>"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(None)
        tail = head

        # while both lists have elements to compare
        while list1 != None and list2 != None:
            next1 = list1.val
            next2 = list2.val

            if next1 <= next2:
                list1 = list1.next
                tail.next = ListNode(next1)
            else: 
                list2 = list2.next
                tail.next = ListNode(next2)
            
            tail = tail.next

        # if either list has any nodes remaining, append to list
        if list1 != None:
            tail.next = list1
        elif list2 != None:
            tail.next = list2

        return head.next


inputs = [
    {
        "list1": ListNode(1, ListNode(2, ListNode(4))),
        "list2": ListNode(1, ListNode(3, ListNode(4)))
    },
    {
        "list1": None,
        "list2": None
    },
    {
        "list1": None,
        "list2": ListNode(0)
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.mergeTwoLists(**input))
