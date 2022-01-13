#Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

tests:
```python
import unittest

from solution import Solution
from solution import ListNode

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one_value(self):
        one = ListNode(1)
        self.assertEqual(self.solution.isPalindrome(one), True)
    def test_isPalindrom(self):
        five = ListNode(3)
        four = ListNode(4, five)
        three = ListNode(5, four)
        two = ListNode(4, three)
        one = ListNode(3, two)
        self.assertEqual(self.solution.isPalindrome(one), True)
if __name__ == "__main__":
    unittest.main()
```

Solution:
```python
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):

        vals = self.get_linked_list_values(head)
        vals_len = len(vals)
        for i in range(vals_len):
            if vals[i] != vals[vals_len - 1 - i]:
                return False
        return True
    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        return result
```

