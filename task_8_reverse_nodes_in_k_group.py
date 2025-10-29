class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy
    while True:
        kth = get_kth(prev_group, k)
        if not kth:
            break
        group_next = kth.next
        prev, curr = kth.next, prev_group.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tmp = prev_group.next
        prev_group.next = kth
        prev_group = tmp
    return dummy.next

def get_kth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

def create_linked_list(values):
    if not values:
        return None
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
    head = create_linked_list([1, 2, 3, 4, 5])
    head = reverseKGroup(head, 2)
    print("Приклад 1:", linked_list_to_list(head))  

    head = create_linked_list([1, 2, 3, 4, 5])
    head = reverseKGroup(head, 3)
    print("Приклад 2:", linked_list_to_list(head)) 
