import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, node))
    dummy = ListNode(0)
    curr = dummy
    while heap:
        _, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
    return dummy.next

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
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    merged = mergeKLists(lists)
    print("Приклад 1:", linked_list_to_list(merged)) 

    lists = []
    merged = mergeKLists(lists)
    print("Приклад 2:", linked_list_to_list(merged)) 

    lists = [create_linked_list([])]
    merged = mergeKLists(lists)
    print("Приклад 3:", linked_list_to_list(merged)) 
