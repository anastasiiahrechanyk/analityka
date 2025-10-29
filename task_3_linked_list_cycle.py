class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def create_linked_list(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    nodes = [head]
    for val in values[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        nodes.append(new_node)
    if pos != -1:
        current.next = nodes[pos]
    return head


if __name__ == "__main__":
    head = create_linked_list([3, 2, 0, -4], 1)
    print("Приклад 1:", hasCycle(head))  # True

    head = create_linked_list([1, 2], 0)
    print("Приклад 2:", hasCycle(head))  # True

    head = create_linked_list([1], -1)
    print("Приклад 3:", hasCycle(head))  # False
