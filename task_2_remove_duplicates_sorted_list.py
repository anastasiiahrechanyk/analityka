class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

def deleteDuplicates(head: ListNode) -> ListNode:
    
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def create_linked_list(values):

    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    # Приклад 1
    head = create_linked_list([1, 1, 2])
    new_head = deleteDuplicates(head)
    print("Приклад 1:", linked_list_to_list(new_head))  # [1, 2]

    # Приклад 2
    head = create_linked_list([1, 1, 2, 3, 3])
    new_head = deleteDuplicates(head)
    print("Приклад 2:", linked_list_to_list(new_head))  # [1, 2, 3]
