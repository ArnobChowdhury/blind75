# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        curr = head
        ls = {}

        i = False
        while curr:
            if curr in ls:
                i = True
                break

            ls[curr] = True
            curr = curr.next

        return i


class Solution2:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


b = ListNode(2)
a = ListNode(1)
a.next = b

sol = Solution()
res = sol.hasCycle(a)
print(res)
