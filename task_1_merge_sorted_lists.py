class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next

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
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    print("Приклад 1:", linked_list_to_list(merged))

    # Приклад 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = mergeTwoLists(list1, list2)
    print("Приклад 2:", linked_list_to_list(merged)) 

    # Приклад 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = mergeTwoLists(list1, list2)
    print("Приклад 3:", linked_list_to_list(merged)) 
