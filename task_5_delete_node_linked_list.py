class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def get_node_by_value(head, value):
    curr = head
    while curr and curr.val != value:
        curr = curr.next
    return curr

if __name__ == "__main__":
    head = create_linked_list([4, 5, 1, 9])
    node = get_node_by_value(head, 5)
    deleteNode(node)
    print("Приклад 1:", linked_list_to_list(head))  # [4, 1, 9]

    head = create_linked_list([4, 5, 1, 9])
    node = get_node_by_value(head, 1)
    deleteNode(node)
    print("Приклад 2:", linked_list_to_list(head))  # [4, 5, 9]
