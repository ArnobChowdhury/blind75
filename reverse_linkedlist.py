class ListNode:
    def __init__(self, value = 0, next = None) -> None:
        self.value = value
        self.next = next

def reverse_linked_list(head):
    curr = head
    next = head.next
    last = None
    
    while curr:
        if next:
            n = next.next
            next.next = curr
        curr = next 

        if next:
            next = n
            last = curr
        
    head.next = None
    print("last", last.value)

c = ListNode(3)
b = ListNode(2, c)
a = ListNode(1, b) 


def print_linkedlist(head):
    curr = head

    while curr:
        print(curr.value)
        curr = curr.next

# print_linkedlist(a)
reverse_linked_list(a)
print("-----------------")

# print_linkedlist(c)
