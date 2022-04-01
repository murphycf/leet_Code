
#143 Reorder List
# have a linked list and want to reorder the linked list
# given L0 -> L1 -> L2 -> L3 -> L4 reorder to L0-> L4_> L2 -> L3
#find the length of the list and reorder the last index's value with the second index's value. reorder the third index's value with the 4th index's value and so on.
#trying to find in 0(n) time
#use pointers. shift one pointer by one and anotehr pointer by 2.

def reorderList(self, head: ListNode) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow.next
        fast.next.next
    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        prev = second
        second = tmp
    #merge two halfs of the list
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

#206 Reverse a Linked List
def reverseList(self, head: ListNode) -> listnode:
    # iterative solution
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def recursiveReverseList(self, head: ListNode) -> listnode:
    #first return the edge case. edge case is empty set.
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None
    return newHead

#203 Remove Linked List Elements
# 1 -> 2 -> 3 -> 4 -> 5 -> 6, val = 6
# 1 -> 2 -> 3 -> 4 -> 5 New List 
def remvoveLinkedListElements(self, head: ListNode) -> listnode:
    dummy = ListNode(next=head)
    prev, curr = dummy, head
    while curr:
        nxt = curr.next
        if curr.val == val:
            prev.next = next
        else:
            prev = curr
        curr = nxt        
    return dummy.next