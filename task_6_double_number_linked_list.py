class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleIt(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    carry = 0
    curr = prev
    new_head = None
    while curr:
        val = curr.val * 2 + carry
        carry = val // 10
        node = ListNode(val % 10)
        node.next = new_head
        new_head = node
        curr = curr.next
    if carry:
        node = ListNode(carry)
        node.next = new_head
        new_head = node
    return new_head

def create_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = create_linked_list([1, 8, 9])
    head = doubleIt(head)
    print("Приклад 1:", linked_list_to_list(head))  # [3, 7, 8]

    head = create_linked_list([9, 9, 9])
    head = doubleIt(head)
    print("Приклад 2:", linked_list_to_list(head))  # [1, 9, 9, 8]






