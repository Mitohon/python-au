#Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

tests:
```python
class TestMiddleOfLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result
    def test_list_length(self):
        three = ListNode(3)
        two = ListNode(2, three)
        one = ListNode(1, two)
        self.assertEqual(self.solution.get_linked_list_length(one), 3)
    def test_one_value(self):
        result = self.solution.middleNode(ListNode(1))
        expected = ListNode(1)
        self.assertEqual(self.get_linked_list_values(result), self.get_linked_list_values(expected))
    def test_odd_number(self):
        three = ListNode(3)
        two = ListNode(2, three)
        one = ListNode(1, two)
        result = self.solution.middleNode(one)
        self.assertEqual(self.get_linked_list_values(result), self.get_linked_list_values(two))
    def test_even_number(self):
        four = ListNode(4)
        three = ListNode(3, four)
        two = ListNode(2, three)
        one = ListNode(1, two)
        result = self.solution.middleNode(one)
        self.assertEqual(self.get_linked_list_values(result), self.get_linked_list_values(three))
```

Solution:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=b=head #a - число, которое движется с шагом 1; b - число, которое движется с шагом 2
        while b and b.next:
            a = a.next
            b = b.next.next

        return a

```

